;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname water-ballon) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;; water-balloon-starter.rkt

; PROBLEM:
; 
; In this problem, we will design an animation of throwing a water balloon.  
; When the program starts the water balloon should appear on the left side 
; of the screen, half-way up.  Since the balloon was thrown, it should 
; fly across the screen, rotating in a clockwise fashion. Pressing the 
; space key should cause the program to start over with the water balloon
; back at the left side of the screen. 
; 
; NOTE: Please include your domain analysis at the top in a comment box. 
; 
; Use the following images to assist you with your domain analysis:
; 
; 
; 1)
; 2).
; .
; 3)
; .
; 4)
; 
; .
;     
; 
; Here is an image of the water balloon:
; (define WATER-BALLOON.)
; 
; 
; 
; NOTE: The rotate function wants an angle in degrees as its first 
; argument. By that it means Number[0, 360). As time goes by your balloon 
; may end up spinning more than once, for example, you may get to a point 
; where it has spun 362 degrees, which rotate won't accept. 
; 
; The solution to that is to use the modulo function as follows:
; 
; (rotate (modulo ... 360) (text "hello" 30 "black"))
; 
; where ... should be replaced by the number of degrees to rotate.
; 
; NOTE: It is possible to design this program with simple atomic data, 
; but we would like you to use compound data.


;; =========
;; Constants:

(define WIDTH 900)
(define HEIGHT 500)

(define CTR-Y (/ HEIGHT 2))

(define WATER-BALLOON.)

(define MTS (empty-scene WIDTH HEIGHT))

;; =========
;; Data Definition

(define-struct ballon(x dx))
;; Ballon is (make-ballon Natural[0, WIDTH] Integer]
;; Interp. (make-ballon x dx) is a ballon with x and dx coordinate
;;        x  : is the center of the ballon
;;        dx : is the coordintae of the ballon
(define B1 (make-ballon 10 2))
(define B2 (make-ballon 20 2))

#;
(define (fn-for-ballon b)
  (... (ballon-x b)  ; Natural[0, WIDTH]
       (ballon-dx b) ; Integer
  ))

;; Templete Ruled Used
;; Compound 2 fields

;; ==========
;; Functions

(define (main b)
  (big-bang b
    (on-tick next-ballon)
    (to-draw render-ballon)
    (on-key handle-key)
    )
  )

;; Tests
(check-expect (next-ballon (make-ballon 10 3)) (make-ballon 13 3))

(check-expect (next-ballon (make-ballon 0 3)) (make-ballon (+ 0 3) 3))

(check-expect (next-ballon (make-ballon WIDTH 3)) (make-ballon (+ WIDTH 3) 3))

;; Ballon -> Ballon
;; produce next Ballon
;(define (next-ballon b) b) ;stub

(define (next-ballon b)
  (make-ballon (+ (ballon-x b) (ballon-dx b)) (ballon-dx b))
  )

;; ======

;; Tests
(check-expect (render-ballon (make-ballon 10 3))
              (place-image (rotate (modulo -10 360) WATER-BALLOON) 10 CTR-Y MTS))

;; Ballo -> Image
;; produce an image of the current ballon
;(define (render-ballon b) b) ;stub
(define (render-ballon b)
  (place-image (rotate (modulo (-(ballon-x b)) 360) WATER-BALLOON) (ballon-x b) CTR-Y MTS)
  )

;; ========
;; Tests
(check-expect (handle-key (make-ballon 0 0) " ") (make-ballon 0 0))

;; KeyEvent, Ballon -> Ballon
;; reset position of the ballon to 0 based on key event
(define (handle-key b ke) (make-ballon 0 (ballon-dx b)))




  