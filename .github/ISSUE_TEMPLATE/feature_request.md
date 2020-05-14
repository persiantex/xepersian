---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: vafakhalighi

---

---

<!---
!! Please fill out all sections !!
-->

## Brief outline of the feature request


## Check/indicate
- [ ] Relevant to the `bidi` package
- [ ] [The `bidi` package issue tracker](https://github.com/persiantex/bidi/issues) has been searched for similar issues?
- [ ] Issue tracker has been searched for similar issues?
- [ ] Links to <tex.stackexchange.com> discussion if appropriate
- [ ] Links to <qa.parsilatex.com> discussion if appropriate

## Minimal example

```tex
% !TEX TS-program = XeLaTeX
% !TEX encoding = UTF-8 Unicode


\documentclass{article}            % or some other class

  % Any packages other than the xepersian package must be loaded here

  % The xepersian package must be loaded as the last package
\usepackage[%
    % Any xepersian package option goes here
]{xepersian}
\settextfont{IRXLotus}

  % Any preamble code goes here
  
\begin{document}

  % Demonstration of feature request here
  
\end{document}
```

## Expected behavior
