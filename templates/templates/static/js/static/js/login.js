async function iniciarSesion() {
    let datos = {
        usuario: txtUsuario.value,
        clave: txtClave.value
    };

    let res = await fetch('/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(datos)
    });

    let respuesta = await res.json();
    if (respuesta.msg === "ok") {
        window.location.href = "/usuarios";
    } else {
        alert("Usuario o clave incorrectos");
    }
}
