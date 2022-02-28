const final = document.getElementById("final");
const btn = document.getElementById("copy-button");

btn.addEventListener("click", copyText);

// CopyText Function
function copyText() {
  console.log(final); //unga unga debug
  final.select();
  document.execCommand("copy");
  btn.textContent = "Copied!";
}
