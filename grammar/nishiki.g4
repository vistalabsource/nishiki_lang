grammar nishiki;

// パーサールール
program: statement* EOF;
statement: expr ';';

expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| INT							# Int
	| '(' expr ')'					# Parens;

// レキサールール
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;

MARKDOWN_COMMENT: '///' ~[\r\n]* -> skip;