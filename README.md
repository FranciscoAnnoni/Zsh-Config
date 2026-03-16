# Configuración de Zsh y iTerm2 (Cross-Platform)

Este repositorio contiene mi configuración personalizada de Zsh, optimizada para macOS (iTerm2) y Linux (Terminator). Incluye temas (Powerlevel10k), plugins y alias para mejorar la productividad.

---

## 🚀 Instalación Automática (Recomendada)

El instalador automático descargará todas las dependencias necesarias (Zsh, fuentes, temas, plugins, terminal) y configurará todo por ti.

### 🐧 Linux (Debian/Ubuntu/Lubuntu)
Ejecuta el siguiente comando en tu terminal:

```bash
# Opción 1: Si ya clonaste el repo
./install_linux.sh

# Opción 2: One-liner (requiere curl)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/FranciscoAnnoni/Zsh-Config/main/install_linux.sh)"
```

### 🍎 macOS
Ejecuta el siguiente comando:

```bash
# Opción 1: Si ya clonaste el repo
./install_mac.sh

# Opción 2: One-liner (requiere curl)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/FranciscoAnnoni/Zsh-Config/main/install_mac.sh)"
```

---

## 🛠 Qué hace el instalador?

1.  **Dependencias:** Instala `zsh`, `git`, `python3`, `ruby`, y la terminal recomendada (`terminator` en Linux, `iterm2` en Mac).
2.  **Fuentes:** Descarga e instala automáticamente las fuentes `MesloLGS NF` requeridas por Powerlevel10k.
3.  **Configuración:**
    *   Restaura `.zshrc`, `.p10k.zsh` y la carpeta `.oh-my-zsh` completa.
    *   Configura el tema visual de la terminal:
        *   **Linux:** Genera automáticamente el archivo de configuración de Terminator con los colores de iTerm2.
        *   **Mac:** Abre el archivo de perfil para importarlo en iTerm2.
4.  **Extras:** Instala la gema `colorls` para listar directorios con iconos.

---

## 📂 Estructura del Proyecto

*   `install_linux.sh`: Script de arranque para Linux. Instala paquetes apt y lanza el configurador.
*   `install_mac.sh`: Script de arranque para macOS. Instala Homebrew/casks y lanza el configurador.
*   `installer.py`: Script principal en Python. Maneja la lógica común (descarga de fuentes, restauración de dotfiles, conversión de colores).
*   `zsh-backup.zip`: Backup comprimido de toda la configuración (.zshrc, plugins, temas).
*   `Francisco.json`: Esquema de colores exportado de iTerm2 (fuente de verdad para los colores).

---

## ⚙️ Instalación Manual (Fallback)

Si el instalador falla, puedes seguir estos pasos:

1.  **Instalar dependencias:**
    *   **Mac:** `brew install zsh romkatv/powerlevel10k/powerlevel10k git ruby`
    *   **Linux:** `sudo apt install zsh git ruby-full terminator`
2.  **Instalar Fuentes:** Descarga e instala `MesloLGS NF` desde [aquí](https://github.com/romkatv/powerlevel10k#manual-font-installation).
3.  **Restaurar Config:**
    *   Descomprime `zsh-backup.zip` en tu home (`~/`).
    *   Asegúrate de que `.zshrc` apunte a la carpeta correcta.
4.  **Configurar Terminal:**
    *   **Mac:** Importa `Francisco.json` en iTerm2 > Profiles > Colors.
    *   **Linux:** Copia el contenido generado en `~/.config/terminator/config`.
5.  **Colorls:** `sudo gem install colorls`.

---
**Nota:** Para desinstalar o revertir, simplemente elimina los archivos `.zshrc`, `.p10k.zsh` y la carpeta `.oh-my-zsh`.
