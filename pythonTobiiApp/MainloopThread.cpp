/* CSS Document */
body,td,th {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: #333333;
}
body {
	background-color: #b8b8b8;
	margin-left: 0px;
	margin-top: 0px;
	margin-right: 0px;
	margin-bottom: 0px;
	text-align: center;
}
*{
	margin: 0;
	padding: 0;
}
.clearfix:after{
	content: ".";
	display: block;
	height: 0;
	clear: both;
	visibility: hidden;
}
.clearfix{
	display: inline-table;
}
/* backslash hack hides from IE mac \*/
* html .clearfix{
	height: 1%;
}
.clearfix {
	display: block;
}
/* end backslash hack */
.clearboth{
	clear: both;
}
.clearfloats{
	clear: both;
}
div#mainwrapper{
	margin: 0 auto;
	width: 522px;
	border: 1px solid #FFF;
	text-align: center;
	background-color: #b8b8b8;
}
div#titlebar{
	height: 33px;
	text-align: left;
	background: #D14200 url("images/tile_titlebarfloat.jpg") repeat-x;
}

div#titlebar h1{
	padding: 5px 10px;
	font-size: 16px;
	color: #FFF;
}
div#subtitlebar{
	margin: 11px auto 0;
	width: 504px;
	height: 26px;
	text-align: left;
	background: #D14200 url("images/subtitlebarfill.gif") no-repeat;
}
div#subtitlebar h1{
	padding: 6px 0 0 16px;
	font-size: 14px;
	color: #FFF;
}
div#contentwrapper{
	margin: 0 auto;
	width: 504px;
	padding-bottom: 10px;
	text-align: left;
	background: #FFF url("images/contentw