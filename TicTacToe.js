// Select the Restart button
var restart = document.querySelector('#btn');

// Select all the Squares
var squares = document.querySelectorAll('td');

// Function to clear the board
function clearBoard(){
  for(var i=0; i < squares.length;i++){
    squares[i].textContent = '';
  }
}

// Clear the board on restart
restart.addEventListener('click',clearBoard);

// Function to check click and change the marker
function changeMarker(){
  if(this.textContent === ''){
    this.textContent ='x';
  }else if (this.textContent === 'x') {
    this.textContent = 'o';
  }else {
    this.textContent = ''
  }
}

// Change the markers in the squares 
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker);
}
