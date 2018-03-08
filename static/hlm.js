document.addEventListener("DOMContentLoaded", () => {
    let nav = document.querySelector(".sidenav")
    let navInstance = M.Sidenav.init(nav)

    let textarea = document.querySelector("textarea")
    let charCounter = M.CharacterCounter.init(textarea)
})
