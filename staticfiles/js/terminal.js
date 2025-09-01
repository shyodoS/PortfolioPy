document.addEventListener('DOMContentLoaded', function () {
    // 1. Inicialização do EmailJS
    emailjs.init('6qlRtRdtPtJ307vPQ'); // Sua Public Key

    // 2. Configurações do serviço
    const serviceID = 'service_za0evvg';
    const templateID = 'template_aomq9la';
    const toEmail = 'marceloshyodos@gmail.com';

    // 3. Elementos do DOM
    const terminalInput = document.getElementById('terminal-input');
    const terminalOutput = document.getElementById('terminal-output');

    // 4. Estado do fluxo
    let step = 'idle';
    let nome = '';
    let contato = '';
    let mensagem = '';

    // 5. Envio do e-mail
    const sendEmail = () => {
        addTerminalLine("guest@marcelo:~$ Enviando mensagem...");

        emailjs.send(serviceID, templateID, {
            to_email: toEmail,
            from_name: nome,
            reply_to: contato,
            message: mensagem
        })
        .then(() => {
            addTerminalLine("guest@marcelo:~$ ✅ E-mail enviado com sucesso!");
        })
        .catch(error => {
            console.error("Erro completo:", error);
            addTerminalLine(`guest@marcelo:~$ ❌ Erro: ${error.text || 'Falha no envio'}`);
        });

        // Reset
        step = 'idle';
        nome = '';
        contato = '';
        mensagem = '';
    };

    // 6. Funções auxiliares
    const addTerminalLine = (text) => {
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.textContent = text;
        terminalOutput.appendChild(line);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    };

    const clearTerminal = () => {
        terminalOutput.innerHTML = '';
        addTerminalLine("guest@marcelo:~$ Terminal limpo");
    };

    const showHelp = () => {
        addTerminalLine("guest@marcelo:~$ Comandos disponíveis:");
        addTerminalLine("- contato → iniciar envio de mensagem");
        addTerminalLine("- clear → limpa o terminal");
        addTerminalLine("- help → mostra esta ajuda");
    };

    // 7. Escutador do terminal
terminalInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        const input = terminalInput.value.trim();
        terminalInput.value = '';

        if (!input) return;

        console.log("Entrada recebida:", input); // <-- Debug
        addTerminalLine(`guest@marcelo:~$ ${input}`);

        const comando = input.toLowerCase();

        switch (step) {
            case 'idle':
                if (comando === 'contato') {
                    step = 'nome';
                    addTerminalLine("guest@marcelo:~$ 📛 Digite seu nome:");
                } else if (comando === 'clear') {
                    clearTerminal();
                } else if (comando === 'help') {
                    showHelp();
                } else {
                    addTerminalLine("guest@marcelo:~$ ❓ Comando não reconhecido. Digite 'help' para ver os comandos.");
                }
                break;

            case 'nome':
                nome = input;
                step = 'contato';
                addTerminalLine("guest@marcelo:~$ 📧 Agora informe seu e-mail ou WhatsApp:");
                break;

            case 'contato':
                contato = input;
                step = 'mensagem';
                addTerminalLine("guest@marcelo:~$ ✏️ Agora escreva sua mensagem:");
                break;

            case 'mensagem':
                mensagem = input;
                sendEmail();
                break;
        }
    }
});


    // 8. Mensagem inicial
    addTerminalLine("guest@marcelo:~$ Bem-vindo ao terminal de contato");
    addTerminalLine("guest@marcelo:~$ Digite 'contato' para iniciar ou 'help' para ver comandos");
});
