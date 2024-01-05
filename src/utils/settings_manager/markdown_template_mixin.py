# Python imports

# Lib imports

# Application imports



class MarkdownTemplateMixin:
    def wrap_html_to_body(self, html):
        return f"""\
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Markdown View</title>
    <style media="screen">
        html, body {{
            display: block;
            background-color: #32383e00;
            color: #ffffff;
            text-wrap: wrap;
        }}
        
        img {{
            width: 100%;
            height: auto;
        }}
        
        code {{
            border: 1px solid #32383e;
            background-color: #32383e;
            padding: 4px;
        }}
    </style>

</head>
<body>

    {html}
    <span>Button in WebView
        <button onclick="say_hello()">Button in WebView</button>
    </span>


    <!-- For internal scripts... -->
    <script src="js/libs/jquery-3.7.1.min.js"></script>

    <!-- For Bootstrap... -->
    <script src="resources/js/libs/bootstrap5/bootstrap.bundle.min.js"></script>

    <!-- For Application... -->
    <script src="resources/js/ui-logic.js"></script>
    <script src="resources/js/post-ajax.js"></script>
    <script src="resources/js/ajax.js"></script>
    <script src="resources/js/events.js"></script>
</body>
</html>

"""
