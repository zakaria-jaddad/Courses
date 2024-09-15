;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname spinning-bears) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; spinning-bears-starter.rkt

(require 2htdp/image)
(require 2htdp/universe)

; PROBLEM:
; 
; In this problem you will design another world program. In this program the changing 
; information will be more complex - your type definitions will involve arbitrary 
; sized data as well as the reference rule and compound data. But by doing your 
; design in two phases you will be able to manage this complexity. As a whole, this problem 
; will represent an excellent summary of the material covered so far in the course, and world 
; programs in particular.
; 
; This world is about spinning bears. The world will start with an empty screen. Clicking
; anywhere on the screen will cause a bear to appear at that spot. The bear starts out upright,
; but then rotates counterclockwise at a constant speed. Each time the mouse is clicked on the 
; screen, a new upright bear appears and starts spinning.
; 
; So each bear has its own x and y position, as well as its angle of rotation. And there are an
; arbitrary amount of bears.
; 
; To start, design a world that has only one spinning bear. Initially, the world will start
; with one bear spinning in the center at the screen. Clicking the mouse at a spot on the
; world will replace the old bear with a new bear at the new spot. You can do this part 
; with only material up through compound. 
; 
; Once this is working you should expand the program to include an arbitrary number of bears.
; 
; Here is an image of a bear for you to use: .


;; =================
;; Constants:
(define HEIGHT 500)
(define WIDTH  500)

(define CTR-Y   (/ HEIGHT 2))
(define CTR-X   (/ WIDTH  2))

(define BEAR .)
(define SPEED 10)

(define MTS (empty-scene WIDTH HEIGHT))

;; =================
;; Data definitions:

(define-struct  bear(x y rotation))
;; bear is make-bear(Natural, Natural)
;; Interp. x is the bear position in the x axis, y is the bear position in the y axis

(define B1 (make-bear 10 10 10))
(define B2 (make-bear CTR-X CTR-Y SPEED))

#;
(define (fn-for-bear b)
  (... (bear-x x)
       (bear-y y)
       ))

;; Teplete rules used
;; - compound: (make-bear Natural Natural)

;; ListOfBear is one of:
;; - empty
;; - (const Bear ListOfBear)
;; Iterp a list of Bears

(define LOB1 empty)
(define LOB2 (cons B1 (cons B2 empty)))

#;
(define (fn-for-lob lob)
  (cond [(empty? lob) (...)]
        [else
         (... (fn-for-bear (first lob))
             (fn-for-lob (rest lob)))]
  ))

;; Template rules used:
;; - one of: 2 cases
;; - atomic distinc: empty
;; - compound: (cons Bear ListOfBear)
;; - reference: (first lob)
;; - slef-reference: (rest lob) is ListOfBear

(define (main lob)
  (big-bang lob                  
    (on-tick advance-lob-rotation)  ; Bear -> Bear
    (to-draw show-bears)         ; Bear -> Image
    (on-mouse handle-mouse)     ; MouseEvent -> Bear
    )
  )

;; ===============
;; Function

;; Bear -> Bear
;; Produce new rotated bear

(check-expect (advance-rotation (make-bear 10 10 10))
              (make-bear 10 10 (+ 10 SPEED)))
(check-expect (advance-rotation (make-bear WIDTH HEIGHT SPEED))
              (make-bear WIDTH HEIGHT (+ SPEED SPEED)))

;(define (advance-rotation b)b) stub

(define (advance-rotation b)
  (make-bear (bear-x b) (bear-y b) (+ (bear-rotation b) SPEED)
  ))

;; ==============

;; ListOfBear -> ListOfBear
;; Produce list of new rotated bear based on the rotation speed

(check-expect (advance-lob-rotation LOB1) empty)

(check-expect (advance-lob-rotation LOB2)
              (cons (make-bear 10 10 (+ 10 SPEED)) (cons (make-bear CTR-X CTR-Y (+ SPEED SPEED)) empty)))

;(define (advance-lob-rotation lob)lob); Stub

(define (advance-lob-rotation lob)
  (cond [(empty? lob) empty]
        [else
         (cons 
          (advance-rotation (first lob))
          (advance-lob-rotation (rest lob)))
         ]
  ))

;; ==============

;; Bear -> Image
;; produce an image of a bear from the given bear struct
(check-expect (show-bear (make-bear 10 10 10))
              (rotate (modulo 10 360) BEAR)
              )

(define (show-bear b)
  (rotate (modulo (bear-rotation b) 360) BEAR) 
  )

(define (get-bear-x-position b)
  (bear-x b)
  )

(define (get-bear-y-position b)
  (bear-y b)
  )

;; ==============

;; ListOfBear -> ListOfImage
;; Produce list of images each image is a bear image
; (define (show-bears lob) lob); Stub

(check-expect (show-bears LOB1) (place-image (rectangle 0 0 "solid" "white") 0 0 MTS))

(check-expect (show-bears LOB2)
              (place-image
               (show-bear (make-bear 10 10 10)) 10 10
               (place-image
                (show-bear(make-bear CTR-X CTR-Y SPEED)) CTR-X CTR-Y
                (place-image (rectangle 0 0 "solid" "white") 0 0 MTS))))

(define (show-bears lob)
  (cond [(empty? lob) (place-image (rectangle 0 0 "solid" "white") 0 0 MTS)]
        [else
         (place-image
          (show-bear (first lob)) (get-bear-x-position (first lob)) (get-bear-y-position (first lob))
           (show-bears (rest lob))
          )
         ]
        )
  )


;; KeyEvent -> ListOfBear
;; Produce new bear from the given event click

(check-expect (handle-mouse (cons (make-bear 10 10 10) empty) 20 20 "button-down")
              (cons (make-bear 10 10 10) (cons (make-bear 20 20 10) empty)))
(check-expect (handle-mouse (cons (make-bear 10 10 10) empty) 20 20 "button-up")
              (cons (make-bear 10 10 10) empty))

(define (handle-mouse w x y key)
  (cond
    [(mouse=? key "button-down") (append w (cons (make-bear x y SPEED) empty))]
    [else w]) 
  )


(main (cons (make-bear CTR-Y CTR-X 0) empty))
