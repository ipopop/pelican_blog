AUTHOR = 'me'
SITENAME = 'azyweb-blog'
# SITEURL = 'https://ipopop.github.io/pelican_blog'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/popdev/pelican-themes/Flex'

PLUGIN_PATHS = ['/Users/popdev/pelican-themes/pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']
