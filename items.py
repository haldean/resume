class Resume:
  def __init__(self):
    self.sections = []

  def add_section(self, section):
    self.sections.append(section)

  def __repr__(self):
    return '\n'.join(map(repr, self.sections))

class Section:
  def __init__(self, title):
    self.title = title
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  @staticmethod
  def from_line(line):
    return Section(line.strip('= \n'))

  def __repr__(self):
    return ')) %s (( \n%s' % (
        self.title, '\n'.join(map(repr, self.items)))

class Description:
  def __init__(self, pairs):
    self.pairs = pairs

  @staticmethod
  def from_lines(lines):
    this_pair = [None, '']
    desc = Description([])
    i = 0

    while i < len(lines):
      line = lines[i].strip('| \n')
      if not line:
        desc.pairs.append(tuple(this_pair))
        this_pair = [None, '']

      elif not this_pair[0]:
        this_pair[0] = line

      else:
        this_pair[1] += ' ' + line

      i += 1
    
    desc.pairs.append(tuple(this_pair))
    return desc

class Item:
  def __init__(self, org, where, what, when):
    self.org = org
    self.where = where
    self.what = what
    self.when = when
    self.subitems = []

  def add_item(self, item):
    item = item.strip('- \n')
    self.subitems.append(item)

  @staticmethod
  def from_line(lines):
    return Item(lines[0].strip('- \n'),
                lines[1].strip(),
                lines[2].strip(),
                lines[3].strip())

  def __repr__(self):
    return '>> %s <<\n-%s\n-%s\n-%s\n%s' % (
        self.org, self.where, self.what, self.when,
        '\n'.join(map(lambda x: '= %s' % x,
                      self.subitems)))


