;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname seat-num-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; seat-num-starter.rkt

; 
; PROBLEM:
; 
; Imagine that you are designing a program to manage ticket sales for a
; theatre. (Also imagine that the theatre is perfectly rectangular in shape!) 
; 
; Design a data definition to represent a seat number in a row, where each 
; row has 32 seats. (Just the seat number, not the row number.)
;  


;; SeatNum is Integer[1, 32]      ; comment that descript new type name 
;[] means inclusive
;() means exclusive

;; interp. seats numbers in a row 1 to 32 seats

(define SN1  1)   ; aisel  ; 3 one or more examples of the data 
(define SN2 23)   ; middle
(define SN3 32)   ; aisel

#;
(define (fn-for-seat-num sn)
  (... sn)
  )

;; Template rules used
;;  - atomic non-distinct: Integer[1, 23]