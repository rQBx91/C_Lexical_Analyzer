import re

class CLexer():
    
    _rule_table = [
        # Comments
        ("\/\*.*?\*\/",     "COMMENT"),
        ("\/\/.*$",         "LINE_COMMENT"),
        ("\/\*.*$",         "MULTILINE_COMMENT_START"),
        ("\*\/",            "MULTILINE_COMMENT_END"),
        # 3-character operators
        ("\<\<\=",          "OP_BITWISE_LSHIFT_ASSIGN"),
        ("\>\>\=",          "OP_BITWISE_RSHIFT_ASSIGN"),
        # 2-character operators
        ("\=\=",            "OPERATOR_EQUALS"),
        ("\!\=",            "OPERATOR_NOT_EQUALS"),
        ("\+\=",            "OPERATOR_ADD_ASSIGN"),
        ("\-\=",            "OPERATOR_SUB_ASSIGN"),
        ("\*\=",            "OPERATOR_MUL_ASSIGN"),
        ("\/\=",            "OPERATOR_DIV_ASSIGN"),
        ("\%\=",            "OPERATOR_MOD_ASSIGN"),
        ("\&\=",            "OPERATOR_AND_ASSIGN"),
        ("\|\=",            "OPERATOR_OR_ASSIGN"),
        ("\^\=",            "OPERATOR_BITWISE_XOR_ASSIGN"),
        ("\>\=",            "OPERATOR_GT_EQUAL"),
        ("\<\=",            "OPERATOR_LT_EQUAL"),
        ("\-\>",            "OPERATOR_STRUCT_DEREF"),
        ("\<\<",            "OPERATOR_BITWISE_LSHIFT"),
        ("\>\>",            "OPERATOR_BITWISE_RSHIFT"),
        ("\&\&",            "OPERATOR_LOGICAL_AND"),
        ("\|\|",            "OPERATOR_LOGICAL_OR"),
        ("\+\+",            "OPERATOR_INC"),
        ("\-\-",            "OPERATOR_DEC"),
        # single-character operators and symbols
        ("\|",              "OPERATOR_BITWISE_OR"),
        ("\!",              "OPERATOR_LOGICAL_NOT"),
        ("\~",              "OPERATOR_BITWISE_NOT"),
        ("\^",              "OPERATOR_BITWISE_XOR"),
        ("\.",              "OPERATOR_STRUCT_REF"),
        ("\?",              "OPERATOR_TERNARY"),
        ("\=",              "OPERATOR_ASSIGN"),
        ("\>",              "OPERATOR_GT"),
        ("\<",              "OPERATOR_LT"),
        ("\/",              "OPERATOR_DIV"),
        ("\%",              "OPERATOR_MOD"),
        ("\:",              "SYMBOL_COLON"),
        ("\;",              "SYMBOL_SEMICOLON"),
        ("\,",              "SYMBOL_COMMA"),
        ("\+",              "SYMBOL_PLUS"),
        ("\-",              "SYMBOL_MINUS"),
        ("\*",              "SYMBOL_STAR"),
        ("\&",              "SYMBOL_AMPERSAND"),
        ("\{",              "SYMBOL_LCB"),
        ("\}",              "SYMBOL_RCB"),
        ("\(",              "SYMBOL_LP"),
        ("\)",              "SYMBOL_RP"),
        ("\[",              "SYMBOL_LB"),
        ("\]",              "SYMBOL_RB"),
        # keywords
        ("auto",            "KEYWORD_AUTO"),
        ("break",           "KEYWORD_BREAK"),
        ("case",            "KEYWORD_CASE"),
        ("char",            "KEYWORD_CHAR"),
        ("const",           "KEYWORD_CONST"),
        ("continue",        "KEYWORD_CONTINUE"),
        ("default",         "KEYWORD_DEFAULT"),
        ("do",              "KEYWORD_DO"),
        ("double",          "KEYWORD_DOUBLE"),
        ("else",            "KEYWORD_ELSE"),
        ("enum",            "KEYWORD_ENUM"),
        ("extern",          "KEYWORD_EXTERN"),
        ("float",           "KEYWORD_FLOAT"),
        ("for",             "KEYWORD_FOR"),
        ("goto",            "KEYWORD_GOTO"),
        ("if",              "KEYWORD_IF"),
        ("inline",          "KEYWORD_INLINE"),
        ("int",             "KEYWORD_INT"),
        ("long",            "KEYWORD_LONG"),
        ("register",        "KEYWORD_REGISTER"),
        ("restrict",        "KEYWORD_RESTRICT"),
        ("return",          "KEYWORD_RETURN"),
        ("short",           "KEYWORD_SHORT"),
        ("signed",          "KEYWORD_SIGNED"),
        ("sizeof",          "KEYWORD_SIZEOF"),
        ("static",          "KEYWORD_STATIC"),
        ("struct",          "KEYWORD_STRUCT"),
        ("switch",          "KEYWORD_SWITCH"),
        ("typedef",         "KEYWORD_TYPEDEF"),
        ("union",           "KEYWORD_UNION"),
        ("unsigned",        "KEYWORD_UNSIGNED"),
        ("void",            "KEYWORD_VOID"),
        ("volatile",        "KEYWORD_VOLATILE"),
        ("while",           "KEYWORD_WHILE"),
        ("_Bool",           "KEYWORD_BOOL"),
        ("_Complex",        "KEYWORD_COMPLEX"),
        ("_Imaginary",      "KEYWORD_IMAGINARY"),
        # Labels
        ("[a-zA-Z_]+\w*?\:","LABEL"),
        # Macros
        ("#define\s.*?$",   "MACRO_DEFINE"),
        ("#undef\s.*?$",    "MACRO_UNDEF"),
        ("#include\s.*?$",  "MACRO_INCLUDE"),
        ("#ifdef\s.*?$",    "MACRO_IFDEF"),
        ("#ifndef\s.*?$",   "MACRO_IFNDEF"),
        ("#endif\s.*?$",    "MACRO_ENDIF"),
        ("#if\s.*?$",       "MACRO_IF"),
        ("#elif\s.*?$",     "MACRO_ELIF"),
        # Constants
        ("\d+",             "NUMERIC_CONSTANT"),
        ("[\'\"].*?[\'\"]", "STRING_CONSTANT"),
        # Identifiers
        ("[a-zA-Z0-9_]+",   "IDENTIFIER"),
        # Whitespace characters (space, tab, newline)
        ("\s+",             "WHITESPACE"),
    ]

    def __init__(self):
        re_list = []
        for e in self._rule_table:
            re_list.append("(?P<%s>%s)" % (e[1], e[0]))
        self.re_tokenizer = re.compile("|".join(re_list))


    def tokenize(self, line):
        position = 0
        tokens = []
        while (position <= len(line)):
            r = self.re_tokenizer.match(line, position)
            if r:
                if r.lastgroup == "WHITESPACE":
                    pass
                else:
                    tokens.append((r.group(r.lastgroup),r.lastgroup, position+1))
                position = r.end()
            else:
                break

        return tokens

