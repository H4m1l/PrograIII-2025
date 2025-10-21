async function guardarUsuario() {
    let datos = {
        usuario: txtUsuario.value,
        clave: txtClave.value,
        nombre: txtNombre.value,
        direccion: txtDireccion.value,
        telefono: txtTelefono.value
    };

    let res = await fetch('/api/usuarios', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(datos)
    });

    let respuesta = await res.json();
    if (respuesta.msg === "ok") {
        alert("Usuario guardado correctamente");
        obtenerUsuarios();
    } else {
        alert("Error al guardar usuario");
    }
}

async function obtenerUsuarios() {
    let res = await fetch('/api/usuarios');
    let usuarios = await res.json();
    let cont = "";
    usuarios.forEach(u => {
        cont += `<p>${u.nombre} - ${u.usuario}
        <button onclick="editar(${u.idUsuario})">Editar</button>
        <button onclick="eliminar(${u.idUsuario})">Eliminar</button></p>`;
    });
    listaUsuarios.innerHTML = cont;
}

async function eliminar(id) {
    if (confirm("¿Eliminar usuario?")) {
        await fetch(`/api/usuarios/${id}`, { method: 'DELETE' });
        obtenerUsuarios();
    }
}
