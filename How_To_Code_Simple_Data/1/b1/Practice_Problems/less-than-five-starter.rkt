;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname less-than-five-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; less-than-five-starter.rkt

; 
; PROBLEM:
; 
; DESIGN function that consumes a string and determines whether its length is
; less than 5.  Follow the HtDF recipe and leave behind commented out versions 
; of the stub and template.
; 


;; String -> Boolean

;; Determines waether the leanght of the given string is less or greater than 5

(check-expect (is-less-than-5 "!") true)
(check-expect (is-less-than-5 "hello, World") false)
(check-expect (is-less-than-5 "hello") false)

;;(define (is-less-than-5 str) 0) ;slub

;(define (is-less-than-5 str)     ;template
;  (...str)
;  )

(define (is-less-than-5 str)
  (< (string-length str) 5)
  )



