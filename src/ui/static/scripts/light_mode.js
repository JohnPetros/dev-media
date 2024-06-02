class LightMode {
  constructor() {
    const toggle = document.querySelector("[data-light-mode='toggle']")
    const elements = document.querySelectorAll("[data-light-mode]")

    if (!toggle || !elements.length) return

    this.currentTheme = localStorage.getItem("@dev-media:theme") ?? "dark"
    this.elements = elements
    this.toggle = toggle

    this.load()
  }

  toggleStoragedTheme() {
    this.currentTheme = this.currentTheme === "dark" ? "light" : "dark"
    localStorage.setItem("@dev-media:theme", this.currentTheme)
  }

  toggleElementsTheme(action) {
    for (const element of this.elements) {
      const lightModeValue = element.dataset.lightMode
      const isToggle = lightModeValue == "toggle"

      if (isToggle) continue

      const lightModeClasses = lightModeValue.split(" ")
      for (const lightModeclass of lightModeClasses) {
        element.classList[action](lightModeclass)
      }
    }
  }

  handleToggleChange() {
    const action = this.currentTheme === "dark" ? "add" : "remove"


    this.toggle.parentNode.classList[action]("text-gray-950")

    this.toggleElementsTheme(action)
    this.toggleStoragedTheme()
  }

  load() {
    if (this.currentTheme == "light") {
      this.toggleElementsTheme("add")
      this.toggle.parentNode.classList.add("text-gray-950")
      this.toggle.checked = true
    }

    this.toggle.addEventListener("change", () => this.handleToggleChange())
  }
}

window.addEventListener("load", () => new LightMode())