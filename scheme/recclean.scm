#!/usr/bin/env sh
exec guile --no-auto-compile -e main -s "$0" "$@"
-*- scheme -*-
!#
(use-modules (ice-9 match))
(use-modules (ice-9 rdelim))
(use-modules (ice-9 popen))
(use-modules (ice-9 textual-ports))

; let-values
(use-modules (srfi srfi-11))
; get-environment-variable
(use-modules (srfi srfi-98))

;; (define (main args))
