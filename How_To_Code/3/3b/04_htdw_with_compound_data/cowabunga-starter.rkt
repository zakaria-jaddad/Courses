;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname cowabunga-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(require 2htdp/image)
; 
; PROBLEM:
; 
; As we learned in the cat world programs, cats have a mind of their own. When they 
; reach the edge they just keep walking out of the window.
; 
; Cows on the other hand are docile creatures. They stay inside the fence, walking
; back and forth nicely.
; 
; Design a world program with the following behaviour:
;    - A cow walks back and forth across the screen.
;    - When it gets to an edge it changes direction and goes back the other way
;    - When you start the program it should be possible to control how fast a
;      walker your cow is.
;    - Pressing space makes it change direction right away.
;    
; To help you here are two pictures of the right and left sides of a lovely cow that 
; was raised for us at Brown University.
; 
; .     .
; 
; Once your program works here is something you can try for fun. If you rotate the
; images of the cow slightly, and you vary the image you use as the cow moves, you
; can make it appear as if the cow is waddling as it walks across the screen.
; 
; Also, to make it look better, arrange for the cow to change direction when its
; nose hits the edge of the window, not the center of its body.
; 


;; ==============
;; Constats
;; ==============

(define WIDTH 500)
(define HEIGHT 500)
(define MIDDLE-Y (/ HEIGHT 2))
(define RIGHT-COW .)
(define LEFT-COW  .)
(define MTS (empty-scene WIDTH HEIGHT))

;; ===============
;; Data Definition
;; ===============

(define-struct cow (x dx))
;; Cow (make-cow Natural[0, WIDTH] Integer)
;; Interp. X postion of the cow and dx is cow's speed

;; Examples
(define C1 (make-cow 0 1))     ; cow going from left to right
(define C2 (make-cow WIDTH -1)) ; cow going from right to left

#;
(define (fn-for-cow cow)
  (...
   (cow-x cow)  ; Natural[0 WIDTH]
   (cow-dx cow) ; Number
   )
  )

;; Template rules used
;; Compouds: 2 fields

;; ===============
;; Data Definition
;; ===============







