import { useEffect, useState } from "react";
import API from "../api";

function Dashboard() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    API.get("/sweets")
      .then((res) => {
        console.log("Sweets data:", res.data);
        setSweets(res.data);
      })
      .catch((err) => {
        console.error("Error fetching sweets:", err);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Sweets</h2>

      {sweets.length === 0 ? (
        <p>No sweets available</p>
      ) : (
        sweets.map((s) => (
          <div key={s.id}>
            <b>{s.name}</b> — ₹{s.price} — Qty: {s.quantity}
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;