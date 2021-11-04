;recursively applies f on x, by first applying f on car x and appending it to 
;recursive call of flatmap on cdr x
(define (flatmap f x)
  (if (null? x) ()
      (append (f (car x)) (flatmap f (cdr x))))
  )

;expand takes in a list and returns a flatmap applying a function depending on if the list equals x or y
(define (expand lst)
  (define (g x)
       (cond ((equal? x 'x) '(x r y f r))
             ((equal? x 'y) '(l f x l y))
             (else (list x))))
         (flatmap g lst))

;flatmap returns a list of instructions instr which are passed into interpret
;if 'f then fd by dist, 'r then rt 90, 'l then lt 90
;recursively calls itself on the rest of the instructions
(define (interpret instr dist)
  (cond ((null? instr) (fd 0))
        ((equal? (car instr) 'f) (begin (fd dist) (interpret (cdr instr) dist)))
        ((equal? (car instr) 'l) (begin (lt 90) (interpret (cdr instr) (dist))))
        ((equal? (car instr) 'r) (begin (rt 90) (interpret (cdr instr) (dist))))
        (else (interpret (cdr instr) dist))))

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))