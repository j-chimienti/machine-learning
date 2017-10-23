const header = `
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Machine Learning</title>
    <base href="/">


    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/x-icon" href="favicon.ico">

    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css"
          integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">

    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"
          integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <style>
      
        
        body {
            font-family: 'Muli', 'Helvetica', 'Arial', 'sans-serif';
            background: whitesmoke;
            margin-top: 5vh;
        }
        

  
    </style>


</head>
<body>

`;
const footer = `
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>



<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js"></script>

</body>
</html>
`;

const navBar = `
<nav>
    <a 
        href="https://jchimienti89.github.io/machine-learning"
    class="btn btn-default pull-right">
        <i class="fa fa-home"></i>
        </a>
</button>
</nav>
`

const navLinks = (path = 'iris.html') => `<div>
  <ul>
    <li>

      <a  class="text-capitalize" href="https://jchimienti89.github.io/machine-learning/${path}#summary">summary</a>
    </li>
    <li><a  class="text-capitalize js-scroll-trigger"  href="https://jchimienti89.github.io/machine-learning/${path}#results">results</a></li>
    <li><a  class="text-capitalize js-scroll-trigger"  href="https://jchimienti89.github.io/machine-learning/${path}#references">references</a></li>
  </ul>
</div>`;

module.exports = {
    header,
    navBar,
    footer,
    navLinks,
};