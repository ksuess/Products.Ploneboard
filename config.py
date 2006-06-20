PROJECTNAME = "Ploneboard"
SKINS_DIR = 'skins'

# Transform config
EMOTICON_TRANSFORM_ID = 'text_to_emoticons'
EMOTICON_TRANSFORM_MODULE = 'Products.Ploneboard.transforms.text_to_emoticons'
URL_TRANSFORM_MODULE = 'Products.Ploneboard.transforms.url_to_hyperlink'
PLONEBOARD_TRANSFORMSCHAIN_ID = 'ploneboard_chain'
PLONEBOARD_TOOL = 'portal_ploneboard'

REPLY_RELATIONSHIP = 'ploneboard_reply_to'
# This should be configurable ttw
NUMBER_OF_ATTACHMENTS = 5

GLOBALS = globals()
