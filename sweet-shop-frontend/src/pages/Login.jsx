import { useState } from "react";
import API from "../api";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    const form = new FormData();
    form.append("username", username);
    form.append("password", password);

    try {
      const res = await API.post("/auth/login", form);
      localStorage.setItem("token", res.data.access_token);
      window.location.href = "/dashboard";
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="auth-box">
      <h2>Login</h2>
      <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={login}>Login</button>
      <p onClick={() => window.location.href="/register"}>New user? Register</p>
    </div>
  );
}