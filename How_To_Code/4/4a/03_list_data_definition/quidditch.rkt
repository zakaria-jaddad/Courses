;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname quidditch) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; quidditch-starter.rkt

; 
; PROBLEM:
; 
; Imagine that you are designing a program that will keep track of
; your favorite dditch teams. (http://iqasport.org/).
; 
; Design a data definition to represent a list of Quidditch teams. 
;    





; 
; 
; 
; 
; (cons "UBC"
;       (cons "MicGil" emty))
;         


;; ListOfString is one of
;; - empty
;; - (cons String ListOfString)
;; Iterp. a list of strings
(define LOS1 empty)
(define LOS2 (cons "MicGil" empty))
(define LOS3 (cons "UBC" (cons "MicGil" empty)))

#;
(define (fn-for-los los)
  (cond [(empty? los) (...)]
        [else
         (... (first los)
              (fn-for-los (rest los)))]))

;; Templete rules used
;; - one of 2 cases
;; - atomic distinct emtyp
;; - cons String ListOfString

; 
; PROBLEM:
; 
; We want to know whether your list of favorite Quidditch teams includes
; UBC! Design a function that consumes ListOfString and produces true if 
; the list includes "UBC".
; 


;; ListOfStrings -> Boolean
;; produce true if UBS in los, fase if UBS not in los
(check-expect (contains-ubc? empty) false)
(check-expect (contains-ubc? (cons "McGill" empty)) false)
(check-expect (contains-ubc? (cons "UBC" empty)) true)
(check-expect (contains-ubc? (cons "McGill" (cons "UBC" empty))) true)

;;(define (contains-ubc? los) false) ;stub
(define (contains-ubc? los)
  (cond [(empty? los) false]
        [else
         (if (string=? (first los) "UBC")
             true
             (contains-ubc? (rest los)))]))