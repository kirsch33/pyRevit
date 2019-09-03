"""Base module for handling extensions parsing."""
from pyrevit import HOST_APP, EXEC_PARAMS

# Extension types
# ------------------------------------------------------------------------------
LIB_EXTENSION_POSTFIX = '.lib'
UI_EXTENSION_POSTFIX = '.extension'


class UIExtensionType:
    ID = 'extension'
    POSTFIX = '.extension'


class LIBExtensionType:
    ID = 'lib'
    POSTFIX = '.lib'


class RUNExtensionType:
    ID = 'run'
    POSTFIX = '.run'


class ExtensionTypes:
    UI_EXTENSION = UIExtensionType
    LIB_EXTENSION = LIBExtensionType
    RUN_EXTENSION = RUNExtensionType

    @classmethod
    def get_ext_types(cls):
        ext_types = set()
        for attr in dir(cls):
            if attr.endswith('_EXTENSION'):
                ext_types.add(getattr(cls, attr))
        return ext_types

    @classmethod
    def is_cli_ext(cls, ext_type):
        """Check if this is a pyRevit CLI extension."""
        return ext_type == cls.RUN_EXTENSION


# -----------------------------------------------------------------------------
# supported scripting languages
PYTHON_LANG = 'python'
CSHARP_LANG = 'csharp'
VB_LANG = 'visualbasic'
RUBY_LANG = 'ruby'
DYNAMO_LANG = 'dynamobim'
GRASSHOPPER_LANG = 'grasshopper'
# cpython hash-bang
CPYTHON_HASHBANG = '#! python3'

# supported script files
PYTHON_SCRIPT_FILE_FORMAT = '.py'
CSHARP_SCRIPT_FILE_FORMAT = '.cs'
VB_SCRIPT_FILE_FORMAT = '.vb'
RUBY_SCRIPT_FILE_FORMAT = '.rb'
DYNAMO_SCRIPT_FILE_FORMAT = '.dyn'
GRASSHOPPER_SCRIPT_FILE_FORMAT = '.gh'
GRASSHOPPERX_SCRIPT_FILE_FORMAT = '.ghx'
CONTENT_FILE_FORMAT = '.rfa'

# extension startup script
EXT_STARTUP_NAME = 'startup'
PYTHON_EXT_STARTUP_FILE = EXT_STARTUP_NAME + PYTHON_SCRIPT_FILE_FORMAT
CSHARP_EXT_STARTUP_FILE = EXT_STARTUP_NAME + CSHARP_SCRIPT_FILE_FORMAT
VB_EXT_STARTUP_FILE = EXT_STARTUP_NAME + VB_SCRIPT_FILE_FORMAT
RUBY_EXT_STARTUP_FILE = EXT_STARTUP_NAME + RUBY_SCRIPT_FILE_FORMAT

# -----------------------------------------------------------------------------
# supported metadata formats
YAML_FILE_FORMAT = '.yaml'
JSON_FILE_FORMAT = '.json'

# metadata filenames
EXT_MANIFEST_NAME = 'extension'
EXT_MANIFEST_FILE = EXT_MANIFEST_NAME + JSON_FILE_FORMAT

DEFAULT_BUNDLEMATA_NAME = 'bundle'
BUNDLEMATA_POSTFIX = DEFAULT_BUNDLEMATA_NAME + YAML_FILE_FORMAT

# metadata schema: Exensions

# metadata schema: Bundles
MDATA_UI_TITLE = 'title'
MDATA_TOOLTIP = 'tooltip'
MDATA_AUTHOR = 'author'
MDATA_AUTHORS = 'authors'
MDATA_LAYOUT = 'layout'
MDATA_COMMAND_HELP_URL = 'help_url'
MDATA_COMMAND_CONTEXT = 'context'
MDATA_MIN_REVIT_VERSION = 'min_revit_version'
MDATA_MAX_REVIT_VERSION = 'max_revit_version'
MDATA_BETA_SCRIPT = 'is_beta'
MDATA_ENGINE = 'engine'
MDATA_ENGINE_CLEAN = 'clean'
MDATA_ENGINE_FULLFRAME = 'full_frame'
MDATA_ENGINE_PERSISTENT = 'persistent'
MDATA_LINK_BUTTON_MODULES = 'modules'
MDATA_LINK_BUTTON_ASSEMBLY = 'assembly'
MDATA_LINK_BUTTON_COMMAND_CLASS = 'command_class'
MDATA_URL_BUTTON_HYPERLINK = 'hyperlink'
MDATA_TEMPLATES_KEY = 'templates'
MDATA_BACKGROUND_KEY = 'background'
MDATA_BACKGROUND_PANEL_KEY = 'panel'
MDATA_BACKGROUND_TITLE_KEY = 'title'
MDATA_BACKGROUND_SLIDEOUT_KEY = 'slideout'
MDATA_HIGHLIGHT_KEY = 'highlight'
MDATA_HIGHLIGHT_NEW_KEY = 'new'
MDATA_HIGHLIGHT_UPDATED_KEY = 'updated'

# metadata schema: Bundles | legacy
UI_TITLE_PARAM = '__title__'
DOCSTRING_PARAM = '__doc__'
AUTHOR_PARAM = '__author__'
AUTHORS_PARAM = '__authors__'
COMMAND_HELP_URL_PARAM = '__helpurl__'
COMMAND_CONTEXT_PARAM = '__context__'
MIN_REVIT_VERSION_PARAM = '__min_revit_ver__'
MAX_REVIT_VERSION_PARAM = '__max_revit_ver__'
SHIFT_CLICK_PARAM = '__shiftclick__'
BETA_SCRIPT_PARAM = '__beta__'
NEW_SCRIPT_PARAM = '__highlight_new__'
UPDATED_SCRIPT_PARAM = '__highlight_updated__'
CLEAN_ENGINE_SCRIPT_PARAM = '__cleanengine__'
FULLFRAME_ENGINE_PARAM = '__fullframeengine__'
PERSISTENT_ENGINE_PARAM = '__persistentengine__'
LINK_BUTTON_ASSEMBLY = '__assembly__'
LINK_BUTTON_COMMAND_CLASS = '__commandclass__'

# -----------------------------------------------------------------------------
# supported bundles
TAB_POSTFIX = '.tab'
PANEL_POSTFIX = '.panel'
LINK_BUTTON_POSTFIX = '.linkbutton'
INVOKE_BUTTON_POSTFIX = '.invokebutton'
PUSH_BUTTON_POSTFIX = '.pushbutton'
SMART_BUTTON_POSTFIX = '.smartbutton'
PULLDOWN_BUTTON_POSTFIX = '.pulldown'
STACK2_BUTTON_POSTFIX = '.stack2'
STACK3_BUTTON_POSTFIX = '.stack3'
STACK_BUTTON_POSTFIX = '.stack'
SPLIT_BUTTON_POSTFIX = '.splitbutton'
SPLITPUSH_BUTTON_POSTFIX = '.splitpushbutton'
PANEL_PUSH_BUTTON_POSTFIX = '.panelbutton'
NOGUI_COMMAND_POSTFIX = '.nobutton'
CONTENT_BUTTON_POSTFIX = '.content'
URL_BUTTON_POSTFIX = '.urlbutton'

# known bundle sub-directories
COMP_LIBRARY_DIR_NAME = 'lib'
COMP_BIN_DIR_NAME = 'bin'
COMP_HOOKS_DIR_NAME = 'hooks'

# unique ids
UNIQUE_ID_SEPARATOR = '-'

# bundle layout elements
DEFAULT_LAYOUT_FILE_NAME = '_layout'
SEPARATOR_IDENTIFIER = '---'
SLIDEOUT_IDENTIFIER = '>>>'

# bundle icon
ICON_FILE_FORMAT = '.png'
DEFAULT_ICON_FILE = 'icon' + ICON_FILE_FORMAT
DEFAULT_ON_ICON_FILE = 'on' + ICON_FILE_FORMAT
DEFAULT_OFF_ICON_FILE = 'off' + ICON_FILE_FORMAT

# bundle media for tooltips
DEFAULT_MEDIA_FILENAME = 'tooltip'

# bundle scripts
DEFAULT_SCRIPT_NAME = 'script'
DEFAULT_CONFIG_NAME = 'config'

# script files
PYTHON_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + PYTHON_SCRIPT_FILE_FORMAT
PYTHON_CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + PYTHON_SCRIPT_FILE_FORMAT

CSHARP_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + CSHARP_SCRIPT_FILE_FORMAT
CSHARP_CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + CSHARP_SCRIPT_FILE_FORMAT

VB_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + VB_SCRIPT_FILE_FORMAT
VB_CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + VB_SCRIPT_FILE_FORMAT

RUBY_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + RUBY_SCRIPT_FILE_FORMAT
RUBY_CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + RUBY_SCRIPT_FILE_FORMAT

DYNAMO_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + DYNAMO_SCRIPT_FILE_FORMAT
DYNAMO_CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + DYNAMO_SCRIPT_FILE_FORMAT

GRASSHOPPER_SCRIPT_POSTFIX = \
    DEFAULT_SCRIPT_NAME + GRASSHOPPER_SCRIPT_FILE_FORMAT
GRASSHOPPER_CONFIG_SCRIPT_POSTFIX = \
    DEFAULT_CONFIG_NAME + GRASSHOPPER_SCRIPT_FILE_FORMAT

GRASSHOPPERX_SCRIPT_POSTFIX = \
    DEFAULT_SCRIPT_NAME + GRASSHOPPERX_SCRIPT_FILE_FORMAT
GRASSHOPPERX_CONFIG_SCRIPT_POSTFIX = \
    DEFAULT_CONFIG_NAME + GRASSHOPPERX_SCRIPT_FILE_FORMAT

# bundle content
DEFAULT_CONTENT_NAME = 'content'
DEFAULT_ALT_CONTENT_NAME = 'other'

CONTENT_POSTFIX = DEFAULT_CONTENT_NAME + CONTENT_FILE_FORMAT
CONTENT_VERSION_POSTFIX = \
    DEFAULT_CONTENT_NAME + "_{version}" + CONTENT_FILE_FORMAT

ALT_CONTENT_POSTFIX = DEFAULT_ALT_CONTENT_NAME + CONTENT_FILE_FORMAT
ALT_CONTENT_VERSION_POSTFIX = \
    DEFAULT_ALT_CONTENT_NAME + "_{version}" + CONTENT_FILE_FORMAT
# -----------------------------------------------------------------------------
# Command bundle defaults
CTX_SELETION = 'selection'
CTX_ZERODOC = ['zero-doc', 'zerodoc']
