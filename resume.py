#!/usr/bin/env python3

import formatters
import argparse
import items

def parse_file(f):
  lines = f.readlines()

  i = 0
  res = items.Resume()
  current_section = None
  current_item = None

  while i < len(lines):
    line = lines[i]
    if line.startswith('=='):
      current_section = items.Section.from_line(line)
      res.add_section(current_section)

    elif line.startswith('--'):
      current_item = items.Item.from_line(lines[i:i+4])
      current_section.add_item(current_item)
      i += 3

    elif line.startswith('-'):
      current_item.add_item(line)

    elif line.startswith(' ') and current_item:
      current_item.subitems[-1] += ' ' + line.strip()

    elif line.startswith('|'):
      start = i
      while line.startswith('|'):
        i += 1
        if i >= len(lines):
          break
        line = lines[i]
      end = i
      i -= 1
      current_section.add_item(
          items.Description.from_lines(lines[start:end]))
    i += 1
    
  return res

def main():
  args = argparse.ArgumentParser(description='Generate resumes')
  args.add_argument('format', help='Format of resume to generate')
  args.add_argument('resume', type=argparse.FileType('r'),
      help='Resume specification')
  args.add_argument('--pre_file', type=argparse.FileType('r'),
      help='The file to insert before the generated output')
  args.add_argument('--post_file', type=argparse.FileType('r'),
      help='The file to insert after the generated output')
  args.add_argument('--output_file', type=argparse.FileType('w'),
      help='The file to write output (if ommited, written to stdout)')
  arg = args.parse_args()

  fmt = formatters.get(arg.format)

  output = ''
  if arg.pre_file:
    output = arg.pre_file.read()

  output += str(fmt(parse_file(arg.resume)))

  if arg.post_file:
    output += arg.post_file.read()

  if arg.output_file:
    arg.output_file.write(output)
  else:
    print(output)

if __name__ == '__main__':
  main()
