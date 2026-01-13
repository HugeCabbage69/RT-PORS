const map = L.map("map").setView([0, 0], 15);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors"
}).addTo(map);

if ("geolocation" in navigator) {
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = pos.coords.latitude;
      const lng = pos.coords.longitude;

      map.setView([lat, lng], 16);

      L.circleMarker([lat, lng], {
        radius: 8,
        color: "red",
        fillColor: "red",
        fillOpacity: 0.9
      }).addTo(map);
    },
    () => alert("no geo")
  );
}
