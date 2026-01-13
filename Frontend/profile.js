const profileB = document.getElementById("profileb");
const profileBlock = document.getElementById("profileblock");

profileB.addEventListener("click", (e) => {
  e.stopPropagation();
  profileBlock.style.display =
    profileBlock.style.display === "block" ? "none" : "block";
});

document.addEventListener("click", () => {
  profileBlock.style.display = "none";
});

function link(route) {
  alert("send: " + route);
}
