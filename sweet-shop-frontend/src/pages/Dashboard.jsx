import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";
import SweetCard from "../components/SweetCard";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);

  const load = () => {
    API.get("/sweets").then(res => setSweets(res.data));
  };

  useEffect(load, []);

  return (
    <>
      <Navbar />
      <div className="container">
        <div className="grid">
          {sweets.map(s => (
            <SweetCard key={s.id} sweet={s} refresh={load} />
          ))}
        </div>
      </div>
    </>
  );
}