import API from "../api";

export default function SweetCard({ sweet, refresh }) {
  const purchase = async () => {
    await API.post(`/sweets/${sweet.id}/purchase`);
    refresh();
  };

  const restock = async () => {
    await API.post(`/sweets/${sweet.id}/restock?amount=5`);
    refresh();
  };

  const remove = async () => {
    await API.delete(`/sweets/${sweet.id}`);
    refresh();
  };

  return (
    <div className="card">
      <h3>{sweet.name}</h3>
      <p>{sweet.category}</p>
      <p>₹{sweet.price}</p>
      <p>Stock: {sweet.quantity}</p>

      <button
        disabled={sweet.quantity === 0}
        onClick={purchase}
      >
        {sweet.quantity === 0 ? "Out of Stock" : "Purchase"}
      </button>

      <button onClick={restock}>Restock +5</button>
      <button style={{ background: "red" }} onClick={remove}>Delete</button>
    </div>
  );
}