import re
import items

formatters = {}
def get(arg):
  if not formatters:
    import inspect
    fmts = filter(
        lambda x: (inspect.isclass(x) and
            issubclass(x, Formatter) and
            x != Formatter),
        globals().values())

    for fmt in fmts:
      formatters[fmt.__name__.lower()] = fmt
  return formatters[arg]

class Formatter:
  def __init__(self, res):
    self.resume = res

  def fmtmatch(self, matchfunc):
    def fmt(match):
      return matchfunc(match.group(1))
    return fmt

  def string(self, line):
    replacements = [
        (r'\*(.*?)\*', self.bold),
        (r'\@(.*?)\@', self.link),
        (r'\_(.*?)\_', self.emph),
        ]

    for pattern, func in replacements:
      line = re.sub(pattern, self.fmtmatch(func), line)
    return self.escape(line)

  def escape(self, line):
    return line

  def items(self, section):
    if not section.items:
      return ''

    def item_repr(item):
      if isinstance(item, items.Item):
        return self.item(item)
      elif isinstance(item, items.Description):
        return self.description(item)
      else:
        return ''

    return '\n'.join(map(item_repr, section.items))

  def __str__(self):
    return '\n'.join(map(self.section, self.resume.sections))

class LaTeX(Formatter):
  def section(self, section):
    if len(section.items) > 1 or (
        len(section.items) == 1 and
        isinstance(section.items[0], items.Item)):
      fmt = '\\resheading{%s}\n\\begin{itemize}%s\n\\end{itemize}' 
    else:
      fmt = '\\resheading{%s}\n%s'

    return fmt % (
        self.string(section.title), self.items(section))

  def item(self, item):
    header ='{%s}{%s}\n{%s}{%s}\n' % (
        self.string(item.org), self.string(item.where),
        self.string(item.what), self.string(item.when))
    if item.subitems:
      header = '\\ressubheading%s{%s}' % (
          header, '\n'.join(map(self.subitem, item.subitems)))
    else:
      header = '\\ressubheadingnoitems' + header

    return header

  def description(self, desc):
    return '\\begin{description}\n%s\n  \\end{description}' % (
       '\n'.join(map(lambda pair: '\\item[\sffamily %s] %s' % pair, desc.pairs)))

  def subitem(self, subitem):
    return '\\resitem{%s}' % self.string(subitem)

  def bold(self, string):
    return '\\textbf{%s}' % string

  def link(self, string):
    return '\\url{%s}' % string

  def emph(self, string):
    return '\\emph{%s}' % string

  def escape(self, line):
    line = line.replace('%', r'\%')
    return line

class HTML(Formatter):
  def section(self, section):
    return '<h2>%s</h2>%s' % (section.title, self.items(section))

  def item(self, item):
    header = '<h3>%s</h3><h4>%s, %s, %s</h4>' % (
        self.string(item.org), self.string(item.what),
        self.string(item.where), self.string(item.when))
    if item.subitems:
      header += '<ul>%s</ul>' % (
          '\n'.join(map(self.subitem, item.subitems)))
    return header

  def subitem(self, subitem):
    return '<li>%s</li>' % self.string(subitem)

  def description(self, desc):
    return '\n'.join(map(lambda pair: '<b>%s:</b>%s' % pair,
                         desc.pairs))

  def bold(self, string):
    return '<b>%s</b>' % string

  def link(self, string):
    return '<a href="%s">[link]</a>' % string

  def emph(self, string):
    return '<i>%s</i>' % string

