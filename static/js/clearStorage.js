let button = document.getElementById("clear-button");
function clearStorage() {
    localStorage.clear();
    alert("cleared local storage!")
}

button.addEventListener("click", clearStorage);
