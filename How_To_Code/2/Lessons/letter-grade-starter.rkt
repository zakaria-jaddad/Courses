;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname letter-grade-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; letter-grade-starter.rkt

; 
; PROBLEM:
; 
; As part of designing a system to keep track of student grades, you
; are asked to design a data definition to represent the letter grade 
; in a course, which is one of A, B or C.
;   

;Here will be tree distinct value either A, B or C
; so we will us the cond for template and because i know what the values might be 

;Enumeration : consists of a fixed number of distinct items

;; LetterGrade is one of:
;;  - "A"
;;  - "B"
;;  - "C"
;; Interp. The Letter Grade In A Course

; For Examples when know it's an Enumeration, When know the Example before the example so for example
; these are not example it's just to understand

; we know that the LetterGrade might be an "A", "B" or "C" --> in this case it's a silly to use them so don't write them

;; <Examples are redondent for Enumerations>

#;
(define (fun-for-letter-grade lg)
  (cond [(string=? lg "A") (...)]
        [(string=? lg "B") (...)]
        [(string=? lg "C") (...)])
  )

;; Template rules used
;; - one of: 3 case
;;  - atomic distinct "A"
;;  - atomic distinct "B"
;;  - atomic distinct "C"



