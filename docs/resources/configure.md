# Configure

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "bitbake": {
      "command": "bitbake-language-server",
      "filetypes": ["bitbake"]
    },
  }
}
```

### [vim-lsp](https://github.com/prabirshrestha/vim-lsp)

```vim
if executable('bitbake-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'bitbake',
          \ 'cmd': {server_info->['bitbake-language-server']},
          \ 'whitelist': ['bitbake'],
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "*.bb", "*.bbappend", "*.bbclass", "*.inc", "conf/*.conf" },
  callback = function()
    vim.lsp.start({
      name = "bitbake",
      cmd = { "bitbake-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "bitbake-language-server")))
  :activation-fn (lsp-activate-on "*.bb" "*.bbappend" "*.bbclass" "*.inc" "conf/*.conf")
  :server-id "bitbake")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "bitbake": {
      "command": [
        "bitbake-language-server"
      ],
      "enabled": true,
      "selector": "source.bitbake"
    }
  }
}
```
