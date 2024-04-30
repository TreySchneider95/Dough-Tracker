var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var li = document.getElementsByTagName("li");
var btn1 = document.getElementById("btn1");

ul.addEventListener("click", function(ev) {
  if (ev.target.tagName === "LI") {
    ev.target.classList.toggle('checked');
  }
}, false);

function inputLength() {
  return input.value.length;
}



function createListElement() {
  var myList = document.getElementsByTagName("li");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(input.value));
  ul.appendChild(li);
  input.value = "";
  var deleteButton = document.createElement("i");

  deleteButton.classList = ['fa fa-trash']
  li.appendChild(deleteButton);
  deleteButton.onclick = function() {
    this.parentElement.remove();
  }
}

function remove(el){
    el.remove()
}

function addListAfterClick() {
  if (inputLength() > 0) {
    createListElement();
  }
}


function addListAfterKeypress() {
  if (inputLength() > 0 && event.keyCode === 13) {
    createListElement();
  }
}

button.addEventListener("click", addListAfterClick);
input.addEventListener("keypress", addListAfterKeypress);


function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
function openAddPartyForm(){
    document.getElementById("partyForm").style.display = "block"
}