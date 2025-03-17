# Configuración de Zsh y iTerm2

Este repositorio contiene mi configuración personalizada de Zsh y iTerm2 para Mac. Incluye temas, plugins y alias para mejorar la productividad en la terminal.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

1. **Homebrew**: El gestor de paquetes para macOS.
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Git:** Para clonar este repositorio.
```brew install git```

## Dependencias

1. Oh My Zsh
Oh My Zsh es un framework para gestionar la configuración de Zsh.
``` sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" ```

2. Powerlevel10k
Un tema personalizado para Zsh que mejora la apariencia del prompt.
``` git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k ```

3. Plugins de Zsh
  - zsh-autosuggestions: Sugiere comandos basados en el historial.
   ``` git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions ```
  - zsh-syntax-highlighting: Resalta la sintaxis de los comandos.
   ``` git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting ```

4. Colorls
Una herramienta para mejorar la visualización de archivos y directorios.
``` sudo gem install colorls ```

### Recomendaciones:
**Fuentes para Powerlevel10k:** 
Powerlevel10k requiere fuentes especiales para mostrar correctamente los iconos y símbolos.
``` 
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font
```

**Visual Studio:** Recordar que cuando configuremos la terminal, la fuente de la terminal debe ser la misma configurada en iterm2 para poder ver los iconos.

-----
-----
# Configuración
1. Clona este repositorio.
2. Copia los archivos de configuración: *Copia .zshrc y .p10k.zsh*
``` 
cp ~/mi-config-zsh/.zshrc ~/.zshrc
cp ~/mi-config-zsh/.p10k.zsh ~/.p10k.zsh

# Copia la carpeta .oh-my-zsh
cp -r ~/mi-config-zsh/.oh-my-zsh ~/.oh-my-zsh
```

