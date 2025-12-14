import { useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";

export default function Admin() {
  const [sweet, setSweet] = useState({
    name: "", category: "", price: "", quantity: ""
  });

  const addSweet = async () => {
    await API.post("/sweets", sweet);
    alert("Sweet added");
  };

  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Add Sweet</h2>
        <input placeholder="Name" onChange={e => setSweet({...sweet, name: e.target.value})} />
        <input placeholder="Category" onChange={e => setSweet({...sweet, category: e.target.value})} />
        <input placeholder="Price" onChange={e => setSweet({...sweet, price: e.target.value})} />
        <input placeholder="Quantity" onChange={e => setSweet({...sweet, quantity: e.target.value})} />
        <button onClick={addSweet}>Add</button>
      </div>
    </>
  );
}