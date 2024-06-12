# Linux

## COMANDOS UNIX

| COMANDO | DESCRIÇÃO | SIGNIFICADO |
| --- | --- | --- |
| -"params" funcao | executa uma função |  |
| ls | lista o seu diretório atual | list |
| cd | entra em outro diretório | change directory |
| mkdir | cria um novo diretório | make directory |
| rmdir | remove um diretório | remove directory |
| rm | apaga um arquivo | remove |
| rm -rf | apaga uma pasta e seus conteúdos |  |
| cp | copia e cola um diretório em algum lugar | copy |
| mv | renomeia arquivo | move |
| exit | fecha o terminal | exit |
| clear | limpa o terminal | clear |
| touch | cria um arquivo vazio |  |
| cat | mostra conteúdo do arquivo | concatenate |
| source | executa um arquivo |  |
| man ou  —help | lê o manual de uma função | manual |
| pwd |  | print working directory |
| whoami |  | who am i |
| >> | joga informação num arquivo |  |
| nano | abre o arquivo no editor Nano |  |
| find | encontra arquivos dentro de uma pasta e suas filhas | find |
| head | mostra primeiras linhas do arquivo | header |
| tail | mostra últimas linhas do arquivo | tail |
| less | carrega o conteúdo do arquivo em partes conforme solicitado |  |
| hostname | mostra o nome da máquina |  |
| hostname -I | mostra o IP da máquina |  |
| ip a |  |  |
| wget | baixa arquivos da web |  |
| grep | filtra o arquivo em busca de uma palavra |  |
| ping | verifica a conexão com um site |  |
| free -h | verifica o uso da memória |  |
| htop | gerenciador de tarefas |  |
| ps | mostra instâncias q estão rodando no terminal |  |
| ps aux | mostra processos que estão rodando no pc, de maneira estática |  |
| lsblk | lista as partições da máquina |  |
| ncdu | escaneia o disco e mostra as pastas do sistema, permitindo apagar e etc. |  |
| lscpu | mostra informações da CPU |  |
| lsusb |  |  |
| curl | realiza requisições http |  |
| dpkg -i | instala arquivo .deb |  |
| ssh-keygen -t ed25519
 |  |  |
| sudo systemctl enable fstrim.timer
  |  |  |
| cat .ssh/id_ed25519.pub |  |  |

## SUPERUSER

| COMANDO | DESCRIÇÃO |
| --- | --- |
| sudo poweroff | desligar o PC |
| sudo apt update | carrega as atualizações |
| sudo apt upgrade | instala as atualizações carregadas |
| sudo apt install "app" | instala uma aplicação |
| sudo apt remove “app” | remove uma aplicação |
| sudo apt -f | conserta instalação quebrada |
| sudo !! | roda o comando anterior como sudo |

## GIT

| COMANDO | DESCRIÇÃO |
| --- | --- |
| git clone | baixa o estado atual de um repositório na nuvem |
| git status | verifica status de versionamento dos arquivos do projeto |
| git add | adiciona arquivos ao commit |
| git commit -m “mensagem” | prepara alterações para enviar |
| git push | envia alterações para a nuvem |
| git pull | baixa alterações mais recentes da nuvem |
| git checkout -b | troca de branch |

### Configurar SSH

| ssh-keygen -t ed25519 | gera chave SSH que conecta com o PC |
| --- | --- |
| sudo systemctl enable fstrim.timer | ? |
| cat .ssh/id_ed25519.pub | printa a chave gerada |

## ATALHOS

| COMANDO | DESCRIÇÃO |
| --- | --- |
| Ctrl L | limpa o terminal |
| Tab | carrega as atualizações |
| ./"app" | executar programa |
| Ctrl + Alt + T | abre terminal |
| Alt + F2 ; xkill  | linha de comando rápida; mata o processo do próximo programa clicado |

## APLICATIVOS LEGAIS

| NOME | DESCRIÇÃO |
| --- | --- |
| rambox | app de tudo junto |
| stacer |  |
| timeshift | backup e drivers |
| chromium-browser | navegador |
| insync |  |
| preload |  |
