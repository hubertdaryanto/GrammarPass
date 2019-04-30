import language_check
tool = language_check.LanguageTool('en-US')


def grammarMatcher(documentText):
    matches = tool.check(documentText)
    len(matches)
