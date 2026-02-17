
def prectal(level, line) :

    if level == 3 :
        match (line) :
            case 0 : return "*"
            case 1 : return "* *"
            case 2 : return "*****"

    half = level // 2
    if line < half :
        # 절반 이하일때
        return prectal(half, line)
    else :
        elli = " " * ((level - line) * 2 - 1 )
        return prectal(half, line - half) + elli + prectal(half, line - half)
    


N = int(input())


for i in range(N) :
    print(prectal(level=N, line=i).center(N*2-1))


"""
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** ***** 

"""