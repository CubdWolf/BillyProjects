#!/usr/bin/racket
#lang racket

(require spd/tags)
(require 2htdp/universe)
(require 2htdp/image)
(@htdw ListOfBall)

(define WIDTH  605)
(define HEIGHT 535)

(define PADDLE-WIDTH 60) 
(define PADDLE-THICKNESS 10)
(define PADDLE (rectangle PADDLE-WIDTH PADDLE-THICKNESS "solid" "white"))
(define PADDLE-CTR-Y (- HEIGHT 40))
(define PADDLE-MOVE-PER-KEY 10)


(define BALL-RADIUS 10)

(define TOP             BALL-RADIUS)
(define BOT (- HEIGHT 1 BALL-RADIUS))
(define LEF             BALL-RADIUS)
(define RIG (- WIDTH  1 BALL-RADIUS))

(define BALL (circle BALL-RADIUS "solid" "white"))

(define MTS (rectangle WIDTH HEIGHT "solid" "green"))


(@htdd Ball)
(define-struct ball (x y dx dy))


(@htdd ListOfBall)


(@htdd Game)
(define-struct game (balls paddle))
(define G0 (make-game (cons (make-ball 0 0 1 1) empty) 0))


(@htdf main)
(define (main g)
  (big-bang g
    (on-draw   render-game)  
    (on-tick   next-game)    
    (on-key    handle-key)    
    (on-mouse  handle-mouse))) 



(@htdf render-game)

(define (render-game g)
  (render-balls (game-balls g) (game-paddle g)))







(@htdf render-balls)

(define (render-balls lob p)
  (cond [(empty? lob)(place-image PADDLE p PADDLE-CTR-Y MTS)]
        [else
         (place-ball (first lob) 
                     (render-balls (rest lob) p))]))



(define (place-ball b img)
  (place-image BALL (ball-x b) (ball-y b) img))




(@htdf next-game)

(define (next-game g)
  (cond [(balls-touch-paddle? (game-balls g)(game-paddle g))
         (game-with-caught-balls g)]
        [else
         (game-with-next-balls g)]))



(@htdf game-with-next-balls)

(define (game-with-next-balls g)
  (make-game (next-balls (game-balls g)) (game-paddle g)))







(@htdf game-with-caught-balls)

(define (game-with-caught-balls g)
  (make-game (next-balls
              (remove-balls
               (game-balls g) (game-paddle g))) (game-paddle g)))




(@htdf remove-balls)
(define (remove-balls lob p)
  (cond [(empty? lob) empty]
        [else (if (touch-paddle? (first lob) p)
                  (remove-balls (rest lob) p)
                  (cons (first lob)(remove-balls (rest lob) p)))]))
      
       

(@htdf next-balls)
(define (next-balls lob)
  (cond [(empty? lob) empty]
        [else
         (cons (next-ball (first lob))
               (next-balls (rest lob)))]))


(@htdf next-ball)
(define (next-ball b)
  (cond [(touch-top?    b) (bounce-top b)]
        [(touch-bottom? b) (bounce-bottom b)]
        [(touch-right?  b) (bounce-right b)]
        [(touch-left?   b) (bounce-left b)]
        [else
         (glide b)]))


(@htdf handle-mouse)
(define (handle-mouse g x y me)
  (cond [(mouse=? me "button-down")
         (make-game
          (cons (make-ball x y (- 5 (random 11))
                           (- 5 (random 11))) (game-balls g))
          (game-paddle g))]
        [else g]))


(@htdf handle-key)

(define (handle-key g ke)
  (cond [(key=? ke " ") (make-game empty (game-paddle g))]
        [(key=? ke "left") (make-game (game-balls g)
                                      (- (game-paddle g) PADDLE-MOVE-PER-KEY))]
        [(key=? ke "right")
         (make-game (game-balls g)
                    (+ (game-paddle g) PADDLE-MOVE-PER-KEY))]     
        [else g]))

(@htdf balls-touch-paddle?)
 

(define (balls-touch-paddle? lob p)
  (cond [(empty? lob) false]
        [else (if (touch-paddle? (first lob) p)
                  true
                  (balls-touch-paddle? (rest lob) p))]))





(@htdf touch-paddle?) 

(define (touch-paddle? b p)
  (and (<= (- p (/ PADDLE-WIDTH 2))
           (ball-x b)
           (+ p (/ PADDLE-WIDTH 2)))
       (<= (- PADDLE-CTR-Y (/ PADDLE-THICKNESS 2))
           (ball-y b)
           (+ PADDLE-CTR-Y (/ PADDLE-THICKNESS 2)))))


(@htdf touch-top?)
(define (touch-top? b)
  (<= (+ (ball-y b) (ball-dy b)) TOP))


(@htdf touch-bottom?)

(define (touch-bottom? b)
  (>= (+ (ball-y b) (ball-dy b)) BOT))


(@htdf touch-left?)

(define (touch-left? b)
  (<= (+ (ball-x b) (ball-dx b)) LEF))


(@htdf touch-right?)

(define (touch-right? b)
  (>= (+ (ball-x b) (ball-dx b)) RIG))


(@htdf bounce-top)

(define (bounce-top b)
  (make-ball (ball-x b) (+ TOP 1) (ball-dx b) (- (ball-dy b))))


(@htdf bounce-bottom)

(define (bounce-bottom b)
  (make-ball (ball-x b) (- BOT 1) (ball-dx b) (- (ball-dy b))))

(@htdf bounce-left)

(define (bounce-left b)
  (make-ball (+ LEF 1) (ball-y b) (- (ball-dx b)) (ball-dy b) ))


(@htdf bounce-right)
(define (bounce-right b)
  (make-ball (- RIG 1) (ball-y b) (- (ball-dx b)) (ball-dy b)))


(@htdf glide)

(define (glide b)
  (make-ball (+ (ball-x b) (ball-dx b))
             (+ (ball-y b) (ball-dy b))
             (ball-dx b)
             (ball-dy b)))

