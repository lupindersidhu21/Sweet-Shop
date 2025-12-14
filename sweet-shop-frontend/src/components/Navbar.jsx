import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Navbar() {
  const { user } = useContext(AuthContext);

  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div style={styles.nav}>
      <h2>🍬 Sweet Shop</h2>
      <div style={styles.divbtn}>
        <button onClick={() => window.location.href="/dashboard"}>Dashboard</button>

        {user?.is_admin && (
          <button onClick={() => window.location.href="/admin"}>Admin</button>
        )}

        <button onClick={logout}>Logout</button>
      </div>
    </div>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px 20px",
    background: "#ff7a00",
    color: "white"
  },
  divbtn: {
    display: "flex",
    justifyContent: "space-between",
    
  }
};