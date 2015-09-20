set nocompatible
:filetype plugin on

" display settings
set showmatch
set showmode
set clipboard=unnamed

syntax enable
highlight Normal ctermfg=grey ctermbg=black
colorscheme wombat 

"set Runtime path to inc Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

"this is the call to begin the Vundle Plugin Opperation

call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'klen/python-mode'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'Lokaltog/vim-easymotion'
Plugin 'sheerun/vim-wombat-scheme'
" Plugin 'gerw/vim-latex-suite'

call vundle#end()
filetype plugin indent on

" key mapings
nmap <C-n> :NERDTreeToggle<CR>

" Easy window switching
nmap <C-h> <C-w>h
let g:C_Ctrl_j = 'off'
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k
nmap <C-l> <C-w>l
set backspace=indent,eol,start

" easier to indent and unintdent code blocks
vnoremap < <gv
vnoremap > >gv

" Set the tab key to put 4 spaces
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab

" Configure Pymode
let pymode_run_bind='<leader>r'
let pymode_python='python3'
let pymode_lint = 1
let pymode_lint_unmodified = 0
let pymode_lint_checkers = ['pyflakes','pep8']
let pymode_rope = 0
