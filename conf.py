# -*- coding: utf-8 -*-

import time

# Data about this site
BLOG_AUTHOR = "Daniel Shapero"  # (translatable)
BLOG_TITLE = "icepack"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://icepack.github.io/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://icepack.github.io/"
BLOG_EMAIL = "shapero@uw.edu"
BLOG_DESCRIPTION = "an ice sheet model in Python"  # (translatable)

# What is the default language?
DEFAULT_LANG = "en"

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 4 theme,
#          may present issues if the menu is too large.
#          (in Bootstrap, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/", "Home"),
        ("/install/", "Install"),
        ("/tutorials/", "Tutorials"),
        ("/how-to/", "How-to"),
        ("/developers/", "Development"),
        ("/contact/", "Contact"),
    ),
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

# Name of the theme to use.
THEME = "base"

# Primary color of your theme. This will be used to customize your theme.
# Must be a HEX value.
THEME_COLOR = '#5670d4'

# Theme configuration. Fully theme-dependent. (translatable)
# Examples below are for bootblog4.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}

# POSTS and PAGES contains (wildcard, destination, template) tuples.
POSTS = (
    ("posts/*.rst", "blog", "post.tmpl"),
    ("posts/*.md", "blog", "post.tmpl"),
    ("posts/*.txt", "blog", "post.tmpl"),
    ("posts/*.html", "blog", "post.tmpl"),
    ("posts/*.ipynb", "blog", "post.tmpl")
)
PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
    ("pages/*.ipynb", "", "page.tmpl")
)

INDEX_PATH = "blog"

# Below this point, everything is optional

# Post's dates are considered in UTC by default
TIMEZONE = "America/Los_Angeles"

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
}

# Enable reST directives that insert the contents of external files such
# as "include" and "raw." This maps directly to the docutils file_insertion_enabled
# config. See: http://docutils.sourceforge.net/docs/user/config.html#file-insertion-enabled
# REST_FILE_INSERTION_ENABLED = True

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Preferred metadata format for new posts
# "Nikola": reST comments, wrapped in a HTML comment if needed (default)
# "YAML": YAML wrapped in "---"
# "TOML": TOML wrapped in "+++"
# "Pelican": Native markdown metadata or reST docinfo fields. Nikola style for other formats.
# METADATA_FORMAT = "Nikola"

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
LOGO_URL = '/images/logo.svg'

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
SHOW_BLOG_TITLE = False

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ['mathjax']

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
# INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
CREATE_SINGLE_ARCHIVE = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = []

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete output/ joe@my.site:/srv/www/site",
#     ]
# }

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# If set to True, any ICC profile will be copied when an image is thumbnailed or
# resized.
# PRESERVE_ICC_PROFILES = False

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).

IMAGE_FOLDERS = {'images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400
# IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False
#
# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
# SHOW_INDEX_PAGE_NAVIGATION = False

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
# META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Set to None to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
#
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# If you need to use the literal braces '{' and '}' in your footer text, use
# '{{' and '}}' to escape them (str.format is used)
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# Create index.html for page folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the PAGE_INDEX
#          will not be generated for that directory.
# PAGE_INDEX = False
# Enable comments on pages (i.e. not posts)?
# COMMENTS_IN_PAGES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
STRIP_INDEXES = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts (not pages!) by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
MATHJAX_CONFIG = """
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
        processEscapes: true
    },
    displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
    "HTML-CSS": {
        styles: {'.MathJax_Display': {"margin": 0}}
    }
});
</script>
"""

# Want to use KaTeX instead of MathJax? While KaTeX may not support every
# feature yet, it's faster and the output looks better.
# USE_KATEX = False

# KaTeX auto-render settings. If you want support for the $.$ syntax (which may
# conflict with running text!), just use this config:
# KATEX_AUTO_RENDER = """
# delimiters: [
#     {left: "$$", right: "$$", display: true},
#     {left: "\\\\[", right: "\\\\]", display: true},
#     {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
#     {left: "$", right: "$", display: false},
#     {left: "\\\\(", right: "\\\\)", display: false}
# ]
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
IPYNB_CONFIG = {
    'TemplateExporter': {
        'exclude_input_prompt': True,
        'exclude_output_prompt': True
    }
}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# Defaults are markdown.extensions.(fenced_code|codehilite|extra)
# markdown.extensions.meta is required for Markdown metadata.
MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Options to be passed to markdown extensions (See https://python-markdown.github.io/reference/)
# Default is {} (no config at all)
# MARKDOWN_EXTENSION_CONFIGS = {}


# Extra options to pass to the pandoc command.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# Pandoc does not demote headers by default.  To enable this, you can use, for example
# ['--base-header-level=2']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="https://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
SHOW_SOURCELINK = False
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# No RSS / Atom
GENERATE_RSS = False
GENERATE_ATOM = False

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '.*\/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.rst'
# (Note the '.*\/' in the beginning -- matches source paths relative to conf.py)
# FILE_METADATA_REGEXP = None

# Should titles fetched from file metadata be unslugified (made prettier?)
# FILE_METADATA_UNSLUGIFY_TITLES = True

# If enabled, extract metadata from docinfo fields in reST documents.
# If your text files start with a level 1 heading, it will be treated as the
# document title and will be removed from the text.
# USE_REST_DOCINFO_METADATA = False

# If enabled, hide docinfo fields in reST document output
# HIDE_REST_DOCINFO = False

# Map metadata from other formats to Nikola names.
# Supported formats: yaml, toml, rest_docinfo, markdown_metadata
# METADATA_MAPPING = {}
#
# Example for Pelican compatibility:
# METADATA_MAPPING = {
#     "rest_docinfo": {"summary": "description", "modified": "updated"},
#     "markdown_metadata": {"summary": "description", "modified": "updated"}
# }
# Other examples: https://getnikola.com/handbook.html#mapping-metadata-from-other-formats

# Map metadata between types/values. (Runs after METADATA_MAPPING.)
# Supported formats: nikola, yaml, toml, rest_docinfo, markdown_metadata
# The value on the right should be a dict of callables.
# METADATA_VALUE_MAPPING = {}
# Examples:
# METADATA_VALUE_MAPPING = {
#     "yaml": {"keywords": lambda value: ', '.join(value)},  # yaml: 'keywords' list -> str
#     "nikola": {
#         "widgets": lambda value: value.split(', '),  # nikola: 'widgets' comma-separated string -> list
#         "tags": str.lower  # nikola: force lowercase 'tags' (input would be string)
#      }
# }

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# Bundle JS and CSS into single files to make site loading faster in a HTTP/1.1
# environment but is not recommended for HTTP/2.0 when caching is used.
# Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Special settings to disable only parts of the indexes plugin.
# Use with care.
# DISABLE_INDEXES = False
# DISABLE_MAIN_ATOM_FEED = False
# DISABLE_MAIN_RSS_FEED = False

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Add the absolute paths to directories containing themes to use them.
# For example, the `v7` directory of your clone of the Nikola themes
# repository.
# EXTRA_THEMES_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = True

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
