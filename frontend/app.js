//@ts-nocheck

// URL del backend Django
const API_URL = "http://127.0.0.1:8000";

// === Vistas ===
const viewLogin = document.getElementById("view-login");
const viewHome = document.getElementById("view-home");
const viewUsuarios = document.getElementById("view-usuarios");

// === Navegación ===
document.getElementById("nav-login").addEventListener("click", () => showView("login"));
document.getElementById("nav-home").addEventListener("click", () => showView("home"));
document.getElementById("nav-usuarios").addEventListener("click", () => {
  showView("usuarios");
  fetchUsuarios();
});

// === Login ===
document.getElementById("btn-login").addEventListener("click", handleLogin);
document.getElementById("btn-logout").addEventListener("click", handleLogout);

// === Usuarios ===
document.getElementById("btn-crear").addEventListener("click", crearUsuario);

const usuariosTableBody = document.querySelector("#usuarios-table tbody");
const welcomeText = document.getElementById("welcome-text");

// === Inicial ===
init();

function init() {
  const email = localStorage.getItem("pq_email");

  if (email) {
    showView("home");
    welcomeText.textContent = `Bienvenido, ${email}`;
  } else {
    showView("login");
  }
}

// === Función Login ===
function handleLogin() {
  const email = document.getElementById("login-email").value.trim();
  const pass = document.getElementById("login-pass").value.trim();

  if (!email || !pass) {
    alert("Ingresa correo y contraseña");
    return;
  }

  localStorage.setItem("pq_email", email);
  welcomeText.textContent = `Bienvenido, ${email}`;
  showView("home");
}

// === Logout ===
function handleLogout() {
  localStorage.removeItem("pq_email");
  document.getElementById("login-email").value = "";
  document.getElementById("login-pass").value = "";
  showView("login");
}

/* ======= CRUD Usuarios ======= */

async function fetchUsuarios() {
  try {
    const res = await fetch(`${API_URL}/usuarios/`, {
      headers: { Accept: "application/json" }
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json();
    renderUsuarios(data);
  } catch (err) {
    console.error("fetchUsuarios:", err);

    usuariosTableBody.innerHTML = `
      <tr>
        <td colspan="5">Error cargando usuarios: ${err.message}</td>
      </tr>
    `;
  }
}

function renderUsuarios(usuarios) {
  usuariosTableBody.innerHTML = "";

  if (!usuarios || usuarios.length === 0) {
    usuariosTableBody.innerHTML = `
      <tr>
        <td colspan="5">No hay usuarios</td>
      </tr>
    `;
    return;
  }

  usuarios.forEach((u) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${u.id ?? ""}</td>
      <td>${escapeHtml(u.nombre ?? "")}</td>
      <td>${escapeHtml(u.correo ?? u.email ?? "")}</td>
      <td>${u.edad ?? ""}</td>
      <td class="actions">
        <button class="edit" data-id="${u.id}">Editar</button>
        <button class="del" data-id="${u.id}">Eliminar</button>
      </td>
    `;

    usuariosTableBody.appendChild(tr);
  });

  document.querySelectorAll(".edit").forEach((btn) =>
    btn.addEventListener("click", onEditar)
  );

  document.querySelectorAll(".del").forEach((btn) =>
    btn.addEventListener("click", onEliminar)
  );
}

// Crear usuario
function crearUsuario() {
  alert("Función crearUsuario aún no implementada");
}

// Editar usuario
function onEditar(e) {
  const id = e.target.dataset.id;
  alert(`Editar usuario ${id} (pendiente)`);
}

// Eliminar usuario
function onEliminar(e) {
  const id = e.target.dataset.id;
  alert(`Eliminar usuario ${id} (pendiente)`);
}

// Escape HTML
function escapeHtml(text) {
  const div = document.createElement("div");
  div.innerText = text;
  return div.innerHTML;
}