function sel(t) {
  document.getElementById("pform").style.display = "none";
  document.getElementById("lform").style.display = "none";

  if (t === "p") document.getElementById("pform").style.display = "flex";
  if (t === "l") document.getElementById("lform").style.display = "flex";
}

function pop(msg) {
  document.getElementById("rpopmsg").innerText = msg;
  document.getElementById("rpopup").style.display = "flex";
}

function closepop() {
  document.getElementById("rpopup").style.display = "none";
}

function sendp() {
  const name = pname.value.trim();
  const phone = pphone.value.trim();
  const addr = paddr.value.trim();
  const desc = pdesc.value.trim();

  if (!name || !phone || !addr || !desc) {
    pop("Fill all fields");
    setTimeout(closepop, 1500);
    return;
  }

  pop("Sending report...");

  setTimeout(() => {
    callerPersonal(name, phone, addr, desc);
  }, 600);
}

function callerPersonal(name, phone, addr, desc) {
  console.log("PERSONAL:", name, phone, addr, desc);

  setTimeout(() => {
    pop("Report sent successfully");
    setTimeout(closepop, 2000);
  }, 1000);
}

function sendl() {
  const issue = lissue.value;

  if (issue === "none") {
    pop("Select an issue first");
    setTimeout(closepop, 1500);
    return;
  }

  pop("Getting location, this may take upto a minute...");

  navigator.geolocation.getCurrentPosition(
    pos => {
      pop("Sending report...");

      setTimeout(() => {
        callerLocal(pos.coords.latitude, pos.coords.longitude, issue);
      }, 700);
    },
    () => {
      pop("Location permission denied");
      setTimeout(closepop, 2000);
    }
  );
}

function callerLocal(lat, lng, issue) {
  console.log("LOCALITY:", lat, lng, issue);

  setTimeout(() => {
    pop("Report sent successfully");
    setTimeout(closepop, 2000);
  }, 1000);
}
