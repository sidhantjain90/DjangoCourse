//Assign Player 1
var player1 = prompt("Enter the Player1 name, You'll be Blue!");
var colorPlayer1 = 'rgb(86, 151, 255)';


//Assign Player 2
var player2 = prompt("Enter the Player2 name, You'll be Red!");
var colorPlayer2 = 'rgb(237, 45, 73)';

//Grabbing table row
var table = $('table tr');

//Reporting a Win
function reportWin(rowNum, colNum){
    console.log("You won starting at this row, col");
    console.log(rowNum);
    console.log(colNum);
}

//Function to change color
function changeColor(rowIndex, colIndex, color){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

//Return the changed/unchanged color
function returnColor(rowIndex, colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// Check the column clicked and then check the corresponding bottom color.
function checkBottom(colIndex){
  var colorReport = returnColor(5, colIndex);
  for(var row=5; row>-1; row--){
    colorReport = returnColor(row,colIndex);
    if(colorReport === 'rgb(128, 128, 128)'){
      return row;
    }
  }
}

// Check to see if 4 neighboring cells are of same color
function colorMatchCheck(one, two, three, four){
  return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

// Win checks
function horizontalWinCheck(){
  for(var row =0; row<6; row++){
    for(var col=0; col<4; col++){
      if(colorMatchCheck(returnColor(row, col), returnColor(row, col+1), returnColor(row, col+2), returnColor(row, col+3))){
        console.log('horiz');
        reportWin(row, col);
        return true;
      }else{
        continue;
      }
    }
  }
}

function verticalWinCheck(){
  for(var col =0; col<7; col++){
    for(var row=0; row<3; row++){
      if(colorMatchCheck(returnColor(row, col), returnColor(row+1, col), returnColor(row+2, col), returnColor(row+3, col))){
        console.log('vertical');
        reportWin(row, col);
        return true;
      }else{
        continue;
      }
    }
  }
}

function diagonalWinCheck(){
  for(var row =0; row<5; row++){
    for(var col=0; col<7; col++){
      if(colorMatchCheck(returnColor(row, col), returnColor(row+1, col+1), returnColor(row+2, col+2), returnColor(row+3, col+3))){
        console.log('diag');
        reportWin(row, col);
        return true;
      }else if(colorMatchCheck(returnColor(row,col), returnColor(row-1, col+1), returnColor(row-2, col+2), returnColor(row-3, col+3))){
        console.log('diag');
        reportWin(row,col);
        return true;
      }else{
        continue;
      }
    }
  }
}


//Game Logic
var currentPlayer =1;
var currentName = player1;
var currentColor = colorPlayer1;

$('h2').text(player1+": it is your turn, pick a column to drop in!");

$('.board button').on('click',function(){
  var col = $(this).closest('td').index();

  var bottomAvail = checkBottom(col);

  changeColor(bottomAvail, col, currentColor);

  if(horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()){
    $('h1').text(currentName+ ", You have won !");
    $('h2').fadeOut('fast');
  }

//  -1 is used just to activate the else condition
  currentPlayer = currentPlayer * -1;

  if(currentPlayer === 1){
    currentName = player1;
    $('h2').text(currentName+", it is your turn");
    currentColor = colorPlayer1;
  }else {
    currentName = player2;
    $('h2').text(currentName+", it is your turn");
    currentColor = colorPlayer2;
  }
})
