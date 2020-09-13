#! /usr/bin/bash

read scripts <<< "$(ls)"
echo $scripts
echo "

<head>
<title>Current Directory</title>
  <style>
  
    body {   
      background-color: rgb(150, 108, 39);    
    }
    
    h1 {
      display: flex;
      justify-content: center;
      color: rgb(255, 200, 53);
    }
    
    .scripts {
      display: flex;
      justify-content: center;
      color: rgb(243, 242, 236);
    }
    
  </style>

</head>
<body>
<h1>Below are the files in the directory that the script is in</h1>
<div class='scripts'>
$scripts
</div>
</body>


" > test.html
xdg-open test.html
sleep 5
rm test.html
