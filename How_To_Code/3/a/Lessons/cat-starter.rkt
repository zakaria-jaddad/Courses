;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname cat-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; cat-starter.rkt

; 
; PROBLEM:
; 
; Use the How to Design Worlds recipe to design an interactive
; program in which a cat starts at the left edge of the display 
; and then walks across the screen to the right. When the cat
; reaches the right edge it should just keep going right off 
; the screen.
; 
; Once your design is complete revise it to add a new feature,
; which is that pressing the space key should cause the cat to
; go back to the left edge of the screen. When you do this, go
; all the way back to your domain analysis and incorporate the
; new feature.
; 
; To help you get started, here is a picture of a cat, which we
; have taken from the 2nd edition of the How to Design Programs 
; book on which this course is based.
; 
; .
; 


(require 2htdp/image)
(require 2htdp/universe)

;; A cat moves from left to right across the sreen 

;; =================
;; Constants:
;; =================

(define WIDTH 900)
(define HEIGHT 700)
(define CTR-Y (/ HEIGHT 2))
(define MTS (empty-scene WIDTH HEIGHT "black"))

(define SPEED 9)

(define CAT-IMG .)

;; =================
;; Data Definition: 
;; =================

;; Cat is Number
;; Interp. X positon of the cat in the sreen coordinate

;; Examples
(define C1 0)            ; cat on the left side of screen 
(define C2 (/ WIDTH 2))  ; cat on the middle of screen
(define C3 WIDTH)        ; cat on the right side of screen


;; Template rulse used
;; - atomic non-distinc: Number
#;
(define (fn-for-cat c)
  (... c)
  ) 



;; =================
;; Functions:
;; =================

;; Signature:
;; Cat -> Cat

;; Porpuse
;; start word with main 0

(define (main c)
  (big-bang c
    (on-tick advance-cat) ; Cat -> Cat
    (to-draw render)      ; Cat -> Image
    (on-key handel-key)   ; cat KeyEvent -> Cat
    )
  )

;; Signature:
;; Cat -> Cat

;; Porpuse:
;; produce next cat by advancing it by SPEED pixle(s) to right

;; Stub
#;
(define (advance-cat c) 0)

;; Tests or Examples

(check-expect (advance-cat 1) (+ SPEED 1))
(check-expect (advance-cat 38) (+ SPEED 38))

;; Definition
(define (advance-cat c)
  (+ c SPEED)
  )


;; Signature
;; Cat -> Image

;; Porpuse:
;; render cat image at appropriate place on MTS(empty screen)

;; Tests
(check-expect (render 4) (place-image CAT-IMG 4 CTR-Y MTS))

;; Stub
(define (render c)
  (place-image CAT-IMG c CTR-Y MTS) 
  )


;=========
;; Signature
;; CAt KeyEvent -> Cat

;; Porpuse
;; Sets The image back to it's initila position after a pressing space

;; Test
(check-expect (handel-key 10 " ") 0)
(check-expect (handel-key 10 "right") 10)

;; Ther is no Stub
(define (handel-key c ke)
  (cond [(key=? ke " ") 0]
        [else c])
  )

;; Run
(main 0)





