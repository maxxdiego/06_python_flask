const createBtn = document.getElementById("createBtn")
const updateBtn = document.getElementById("updateBtn")
createBtn.addEventListener("click", createGame)
updateBtn.addEventListener("click", updateGame)

function createGame() {

  const form = document.getElementById("createForm");
  form.addEventListener("submit", function(event) {
  event.preventDefault(); // Evita o envio padrão do formulário
  })

  const tituloInput = document.getElementById("titulo")
  const descricaoInput = document.getElementById("descricao")
  const anoInput = document.getElementById("ano")

  const game = {
    titulo: tituloInput.value,
    descricao: descricaoInput.value,
    ano: anoInput.value,
  }
  axios
    .post("http://localhost:5000/games", game)
    .then((response) => {
      if (response.status == 201) {
        alert("Game cadastrado!")
        location.reload()
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

// createGame()

function deleteGame(listItem) {
    const id = listItem.getAttribute("data-id")
    axios.delete("http://localhost:5000/games/" + id).then(response => {
        alert("Game deletado!")
        location.reload()
    }).catch(err => {
        console.log(err)
    })
}

function loadForm(listItem) {
  const id = listItem.getAttribute("data-id")
  const titulo = listItem.getAttribute("data-titulo")
  const ano = listItem.getAttribute("data-ano")
  const descricao = listItem.getAttribute("data-descricao")
  document.getElementById("idEdit").value = id
  document.getElementById("tituloEdit").value = titulo
  document.getElementById("anoEdit").value = ano
  document.getElementById("descricaoEdit").value = descricao
}

function updateGame() {

  const form = document.getElementById("editForm");
  form.addEventListener("submit", function(event) {
  event.preventDefault(); // Evita o envio padrão do formulário
  })

  const idInput = document.getElementById("idEdit")
  const tituloInput = document.getElementById("tituloEdit")
  const anoInput = document.getElementById("anoEdit")
  const descricaoInput = document.getElementById("descricaoEdit")

  const game = {
    titulo: tituloInput.value,
    descricao: descricaoInput.value,
    ano: anoInput.value
  }

  var id = idInput.value

  axios
    .put("http://localhost:5000/games/" + id, game)
    .then((response) => {
      if (response.status == 200) {
        alert("Game atualizado!")
        location.reload()
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

axios
  .get("http://localhost:5000/games")
  .then((response) => {
    const games = response.data
    const list = document.getElementById("games")

    games.forEach((game) => {
      let item = document.createElement("li")

      item.setAttribute("data-id", game._id)
      item.setAttribute("data-titulo", game.titulo)
      item.setAttribute("data-ano", game.ano)
      item.setAttribute("data-descricao", game.descricao)

      item.innerHTML = `<h3>${game.titulo}</h3>
        <p>Descrição: ${game.descricao}</p> 
        <p>Ano: ${game.ano}</p>
        <p>ID: ${game._id}</p>`

      var deleteBtn = document.createElement("button")
      deleteBtn.innerHTML = "Deletar"
      deleteBtn.classList.add("btn")
      deleteBtn.classList.add("btn-danger")
      deleteBtn.classList.add("mb-3")
      deleteBtn.addEventListener("click", function(){
        deleteGame(item)
      })

      var editBtn = document.createElement("button")
      editBtn.innerHTML = "Editar"
      editBtn.classList.add("btn")
      editBtn.classList.add("btn-warning")
      editBtn.classList.add("mb-3")
      editBtn.addEventListener("click", function(){
        loadForm(item)
      })
  
      item.appendChild(deleteBtn)
      item.appendChild(editBtn)
      list.appendChild(item)
    })
  })
  .catch((error) => {
    console.log(error)
  })
