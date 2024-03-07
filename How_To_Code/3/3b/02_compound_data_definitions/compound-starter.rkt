;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname compound-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; compound-starter.rkt

; 
; PROBLEM:
; 
; Design a data definition to represent hockey players, including both 
; their first and last names.
; 



(define-struct player (fn ln))
;; Player is (make-player String String)
;; Interp. (make-palyer fn ln) is a hockery player where
;; - fn is player first name
;; - ln is player last name

(define P1 (make-player "Zakaria" "Jaddad"))

(define (fn-for-player p)
  (... (player-fn p)   ; String
       (palyer-ln p )  ; String
       ) 
  )