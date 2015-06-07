Wind Stabilization of a UAV
	People
		Randal W. Beard
			ECE Professor at Brigham Young University (Provo, UT)
			Background
				Ph.D. in electrical engineering from 
				Rensselaer Polytechnic Institute in Troy NY
				
				Senior member of the IEEE
				Senior member of AIAA
				Associate Editor for the IEEE Control Systems Magazine
				and for the Journal of Intelligent and Robotic Systems
			Current Research Interests 
				autonomous systems, unmanned air vehicles, and
				multiple vehicle coordination and control
			Books/Articles
				Small Unmanned Aircraft: Theory and Practice
				Fixed  Wing  UAV  Path  Following  in  Wind  with
					Input  Constraints
				Relative  Navigation  Approach  for  Vision-
					Based Aerial GPS-Denied  Navigation
			Contact
				801-422-8392
				beard@byu.edu
		Timothy W. McLain
			Mechanical Engineering Professor at Brigham Young University (Provo, UT)
			Background
				Ph.D. in mechanical engineering from
				Stanford University
				
				Director of the NSF-sponsored Center
				for Unmanned Aircraft Systems (C-UAS)
			Current Research Interests
				Dynamic systems, control system design; guidance, dynamics,
				control, and autonomy of unmanned aircraft systems
			Books/Articles
				Small Unmanned Aircraft: Theory and Practice
				A Radar-Based, Tree-Branching Sense and Avoid System
					for Small Unmanned Aircraft
				Tailsitter attitude control using resolved tilt-twist
				Differential flatness based control of a rotorcraft 
					for aggressive maneuvers
			Contact
				mclain@byu.edu
	Articles/Books
		chronological
		
			Sept 2007
			Flight Dynamics Principles, 2nd Edition
		
			Feb 2012
			Small Unmanned Aircraft: Theory and Practice
		
			Feb 2014
			Fixed Wing UAV Path Following in Wind With Input Constraints 
		alphebetical
			Fixed Wing UAV Path Following in Wind With Input Constraints
				http://www.et.byu.edu/~beard/papers/preprints/BeardFerrinHumpherys__.pdf
				Authors
					Randal W. Beard
					Jeff Ferrin (Ph.D. Student)
					Jeffrey Humphreys (Professor of Mathematics)
				Abstract
					This paper considers the problem of fixed wing
					unmanned air vehicles following straight lines
					and orbits. To account for ambient winds, we use a
					path following approach as opposed to trajectory
					tracking. The unique feature of this paper is that
					we explicitly account for roll angle constraints
					and flight path angle constraints. The guidance laws
					are derived using the theory of nested saturations,
					and explicit flight conditions are derived that
					guarantee convergence to the path. The method is
					validated by simulation and flight tests.
			Flight Dynamics Principles, 2nd Edition
				Ch 9 on stability
			Small Unmanned Aircraft: Theory and Practice
				http://proquest.safaribooksonline.com.proxy.mul.missouri.edu/9780691149219
				Authors
					Randal W. Beard
					Timothy W. McLain
				Abstract
					Autonomous unmanned air vehicles (UAVs) are critical to current
					and future military, civil, and commercial operations. Despite
					their importance, no previous textbook has accessibly introduced
					UAVs to students in the engineering, computer, and science
					disciplines--until now. Small Unmanned Aircraft provides a
					concise but comprehensive description of the key concepts and
					technologies underlying the dynamics, control, and guidance of
					fixed-wing unmanned aircraft, and enables all students with an
					introductory-level background in controls or robotics to enter
					this exciting and important area.

					The authors explore the essential underlying physics and sensors 
					of UAV problems, including low-level autopilot for stability and 
					higher-level autopilot functions of path planning. The textbook
					leads the student from rigid-body dynamics through aerodynamics,
					stability augmentation, and state estimation using onboard sensors,
					to maneuvering through obstacles. To facilitate understanding, the
					authors have replaced traditional homework assignments with a
					simulation project using the MATLAB/Simulink environment. Students
					begin by modeling rigid-body dynamics, then add aerodynamics and
					sensor models. They develop low-level autopilot code, extended
					Kalman filters for state estimation, path-following routines, and
					high-level path-planning algorithms. The final chapter of the book
					focuses on UAV guidance using machine vision.
				Summary
					Ch 2: Coordinate Frames
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Rotation Matrices - Matrix that, when multiplied, rotates one set of vector components 
						to another set.
						
						R(01) = rotation from coordinate frame F0 to F1
						ex. p1 = R(01)*p0
						
						R(01) can be written as
						.            ( cos(theta)  sin(theta)  0)
						.    R(01) = (-sin(theta)  cos(theta)  0)
						.			 (     0            0      1)
						Location of the rows depends on where the rotation is taking place, however, the negative
						sine term always appears above the row with just 0's and 1's
						
						Properties of Rotation Matrices:
						R(01)^-1 = R(01)T = R(10)
						R(bc)*R(ab) = R(ac)
						det(R(ab)) = 1
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						MAV Coordinate Frames:
						Inertial Frame (Fi) - earth fixed reference frame. Commonly x direction points North, y
						direction points East and z direction points Down and is therefore sometimes refered to
						as the north-east-down (NED) reference frame. Origin is as a defined home location.
						
						Vehicle Frame (Fv) - origin is at the center of mass of the vehicle and the axes are 
						alligned with the intertial frame (north,east and down directions).
						
						Vehicle 1 Frame (Fv1) - origin is at the center of mass of the vehicle. The z direction
						is the same as in the vehicle frame (down) but the x direction points out the nose of the 
						plane and the y direction points along the right wing. The right hand rotation around the
						z axis that changes Fv to Fv1 is given by the heading angle (yaw) written as psi.
						
						Vehicle 2 Frame (Fv2) - Origin is at the center of mass of the vehicle. The x and y 
						directions still point out of the nose and right wing but now the z direction points out 
						of the belly of the aircraft. The y direction is still horizontal whereas the x direction 
						is no longer parallel with the "flat" ground. The rotation around the y axis that produces
						this frame from Fv1 is defined by the pitch angle, theta.
						
						Body Frame (Fb) - Origin is at the center of mass of the vehicle. The x, y and z directions
						point out of the nose, wing and belly. Now all of these directions are directly out of these 
						parts of the aircraft and are no longer defined as being parallel or perpendicular with the 
						horizontal plane. The rotation around the x axis that gives Fb from Fv2 is defined by the 
						roll angle, phi.
						
						Stability Frame (Fs) - origin at the center of mass of the vehicle. This axis is the same as
						the body axis with a left-hand rotation around the y direction defined by the angle of attack,
						alpha. The is vector will line up with the projection of the airspeed vector, Va, on the plane
						created by ib and kb.
						
						Wind Frame (Fw) - origin at the center of mass of the vehicle. This axis is the rotation around
						the z axis that puts the airspeed vector, Va, in the plane created by ib and kb. The angle of the
						roatation is called the side-slip angle (beta).
						
						
						The rotation matrix that brings the vehicle axis to the body axis is given as
						.    R(vb)(phi,psi,theta) = R(v,v1)(psi)*R(v1,v2)(theta)*R(v2,b)(phi)
						
						The rotations that bring the body axis to the stability and wind frames are given as
						.    R(bw)(alpha,beta) = R(bs)(alpha)*R(sw)(beta)
						
						yaw (psi) = rotation around z axis
						pitch (theta) = rotation around y axis
						roll (phi) = rotation around x axis
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Airspeed, Wind Speed and Ground Speed
						
						Ground Speed (Vg) - Speed of the air vehicle relative to the inertial frame
						Airspeed (Va) - Speed of the air vehicle relative to the surrounding air
						Wind Speed (Vw) - Wind velocity relative to the inertial frame
						
						The three velocities are related by
						.   Va = Vg - Vw
						
						All three vectors in the body frame
						.           (u)
						.   V(gb) = (v) 
						.           (w)
						
						.           (uw)                          (wn)
						.   V(wb) = (vw) = R(vb)(phi,theta,psi) * (we)
						.           (ww)                          (wd)
						
						.           (ur)   (u - uw)
						.   V(ab) = (vr) = (v - vw)
						.           (wr)   (w - ww)
						
						Additional expressions
						.   Va = sqrt(ur^2 + vr^2 + wr^2)
						.   alpha (angle of attack) = arctan(wr/ur)
						.   beta (side slip angle) = arcsin(vr/Va)
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						The Wind Triangle
						
						Flight Path Angle (gamma) - angle between the horizontal and Vg vector
						Course Angle (chi) - Angle between the projection of Vg on the horizontal plane and true north
						
						The Wind Triangle is given by the Vg, Va and Vw vectors by the relation
						.   Va = Vg - Vw
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Differentiation of a Vector
						
						If there is a vector p moving in a frame Fb and that frame Fb is rotating (but not 
						translating) relative to another frame Fi, then the time derivative of p in frame Fi is
						given by
						
						.     d       d
						.    dti p = dtb p + w(b/i) x p
						
						where the first term is shows how vector p changes relative to frame Fb and the second
						term shows how Fb changes relative to Fi. The term w(b/i) is the angular velocity of frame
						Fb in frame Fi.
					Ch 3: Kinematics and Dynamics 
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						State Variables - There are 12 state variables to fully define the equations of motion
						of a MAV.
						
						pn = Inertial north position of the MAV along ii in Fi
						pe = Inertial east position of the MAV along ji in Fi
						pd = Inertial down position (negative of altitude) of the MAV measured along ki in Fi
						u = Body frame velocity measured along ib in Fb
						v = Body frame velocity measured along jb in Fb
						w = Body frame velocity measured along kb in Fb
						phi = Roll angle defined with respect to Fv2
						theta = Pitch angle defined with respect to Fv1
						psi = Heading (yaw) angle defined with respect to Fv
						p = Roll rate measured along ib in Fb
						q = Pitch rate measured along jb in Fb
						r = Yaw rate measured along kb in Fb
							
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Kinematics
						
						Translational velocity commonly given in body frame (u,v,w)
						Translational position commonly given in inertial reference frame (pn,pe,pd)
						These two sets of variables are related by a derivative and a rotation
						.       (pn)         (u)
						.     d (pe) = R(bv) (v)
						.    dt (pd)         (w)     (rotation matrix expanded in Equation 3.1)
						
						The angular rates are defined in the body frame but the Euler angles are all defined
						in different frames. Relating the body frame angular rates to the derivatives of the
						Euler Angles gives
						.    (p)   (phi_dot)             (    0    )                        (   0   )
						.    (q) = (   0   ) + R(v2,b) * (theta_dot) + R(v2,b) * R(v1,v2) * (   0   )
						.    (r)   (   0   )             (    0    )                        (psi_dot)
						
						or
						.    (p)   (1    0          -sin(theta)     )   ( phi_dot )
						.    (q) = (0  cos(phi)  sin(phi)*cos(theta)) * (theta_dot)
						.    (r)   (0 -sin(phi)  cos(phi)*cos(theta))   ( psi_dot )  (inverse given by Equation 3.3)
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Dynamics
						
						Translational Motion
						- Manipulating Newton's second law by changing the time derivative of the ground speed
						from the inertial frame to the body frame and expressing the forces and velocities in
						the body frame we get
						.        (dV(gb)     b       b)
						.    m * ( dtb   + w(b/i) x Vg) = fb
						
						where the time derivative term is the derivative of the ground speed in the body 
						frame (u_dot,v_dot,w_dot), the w(b/i) term is the angular rates in the body axis (p,q,r)
						and the fb term is the sum of the externally applied forces in the body frame components.
						The relation can therefore be rewritten as
						.   (u_dot)   (rv-qw)           (fx)
						.   (v_dot) = (pw-ru) + (1/m) * (fy)
						.   (w_dot)   (qu-pv)           (fz)
						
						
						Rotational Motion
						Starting from Newtons second law, changing the variables to the body frame and taking into
						account the symmetry of aircraft about the plane formed by ib and kb the angular accelerations
						can be represented as
						.    (p_dot)   (Gamma1*p*q - Gamma2*q*r + Gamma3*l + Gamma4*n)
						.    (q_dot) = (     Gamma5*p*r - Gamma6*(p^2-r^2) + m/Jy    )
						.    (r_dot)   (Gamma7*p*q - Gamma1*q*r + Gamma4*l + Gamma8*n)
						
						where the moments acting on the body axes are mb = (l,m,n) and the different Gamma's are given by
						.    Gamma1 = Jxz*(Jx-Jy+Jz)/Gamma
						.    Gamma2 = (Jz*(Jz-Jy)+Jxz^2)/Gamma
						.    Gamma3 = Jz/Gamma
						.    Gamma4 = Jxz/Gamma
						.    Gamma5 = (Jz-Jx)/Jy
						.    Gamma6 = Jxz/Jy
						.    Gamma7 = ((Jx-Jy)*Jx+Jxz^2)/Gamma
						.    Gamma8 = Jx/Gamma
						
						and Gamma = Jx * Jz - Jxz^2
					Ch 4: Forces and Moments
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Gravitational Forces
						Rotating the gravitational force from the ki axis to the body frame gives
						.                    (0 )   (    -m*g*sin(theta)    )
						.    f(gb) = R(vb) * (0 ) = (m*g*cos(theta)*sin(phi))
						.                    (mg)   (m*g*cos(theta)*cos(phi))
						
						There are no moments produced by the gravitational force because it acts through the 
						center of mass of the MAV.
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Aerodynamic Forces and Moments
						
						Control Surfaces
						- Ailerons (delta_a) are used to control the roll angle (phi)
						- Elevators (delta_e) are used to control the pitch angle (theta)
						- Rudders (delta_r) are used to control the yaw angle (psi)
						
						Since there are two ailerons that rotate different directions the deflection delta_a is
						a composite and is written as 
						.    delta_a = 1/2*(delta_a_left - delta_a_right)
						
						Positive deflections are given by using the right hand rule on the hinge axes of the 
						control surfaces (ib,jb,kb)
						
						
						Longitudinal Aerodynamics
						The lift and drag forces and the pitching moment form the longitudinal aerodynamics of
						a MAV. When the lift and drag forces are rotated from the stability frame to the body
						frame they can be modeled as
						.    (fx)                ([-CD(alpha)*cos(alpha)+CL(alpha)*sin(alpha)]+c/(2*Va)*q*[-CDq*cos(alpha)+CLq*sin(alpha)]+delta_e*[-CDdelta_e*cos(alpha)+CLdelta_e*sin(alpha)])
						.    (fz) = rho*Va^2*S/2*([-CD(alpha)*sin(alpha)-CL(alpha)*cos(alpha)]+c/(2*Va)*q*[-CDq*sin(alpha)-CLq*cos(alpha)]+delta_e*[-CDdelta_e*sin(alpha)-CLdelta_e*cos(alpha)])
						where CD(alpha) and CL(alpha) can be expressed as a more accurate non-linear model or
						linearized but lose fidelity at higher angles of attack
						
						Non-linear CD(alpha) and CL(alpha)
						.    CD(alpha) = CDp + ((CL0 + CLalpha*alpha)^2)/(pi*e*AR)
						.    CL(alpha) = (1-sigma(alpha))*[CL0+CLalpha*alpha]+sigma(alpha)*[2sign(alpha)*sin(alpha)^2*cos(alpha)]
						where
						.                    1 + e^(-M*(alpha-alpha0)) + e^(M*(alpha-alpha0))
						.    sigma(alpha) = (1+e^(-M*(alpha-alpha0)))*(1+e^(M*(alpha-alpha0)))
						where M and alpha0 were positive constants
						
						Linear CD(alpha) and CL(alpha)
						.    CD(alpha) = CD0 + CDalpha * alpha
						.    CL(alpha) = CL0 + CLalpha * alpha  (keep in mind these are inaccurate for large alpha)
						
						The pitching moment is linearized with alpha for the purposes of this model. A more complex
						model would have to be determined by a wind tunnel or flight experiments. The pitching 
						moment can be given as
						.    m = 1/2*rho*Va^2*S*c*[Cm0 + Cmalpha + Cmq*c/(2*Va)*q + Cmdelta_e*delta_e]
						where c is the mean chord of the MAV wing.
						
						Lateral Aerodynamics
						The force along the jb axis and the roll and yaw moments (l and n) define the lateral
						aerodynamics. These can be given by
						.    fy = 1/2*rho*Va^2*S*[CY0 + CYbeta*beta + CYp*b/(2*Va)*p + CYr*b/(2*Va)*r + CYdelta_a*delta_a + CYdelta_r*delta_r]
						.    l = 1/2*rho*Va^2*S*b*[Cl0 + Clbeta*beta + Clp*b/(2*Va)*p + Clr*b/(2*Va)*r + Cldelta_a*delta_a + Cldelta_r*delta_r]
						.    n = 1/2*rho*Va^2*S*b*[Cn0 + Cnbeta*beta + Cnp*b/(2*Va)*p + Cnr*b/(2*Va)*r + Cndelta_a*delta_a + Cndelta_r*delta_r]
						where CY0, Cl0 and Cn0 are typically zero for symmetric aircraft
						
						
						Aerodynamic Coefficients
						
						Static stability derivatives determine if when a MAV is put off of its normal flight 
						conditions the moments on the MAV tend to restore it to its nominal flight condition.
						Cmalpha is the longitudinal stability derivative and must be negative for the MAV to
						be statically stable. Clbeta is the roll static stability derivative and must be
						negative for the MAV to be statically stable. Cnbeta is the yaw static stability
						derivative and must be positive for the MAV to be statically stable.
						
						Dynamic stability derivatives determine if when a disturbance is applied to a MAV if 
						the response of the MAV damps out over time. If a mass spring damper system analogy 
						is used the static stability derivatives act like torsional springs and the dynamic
						stability derivatives (Cmq, Clp, Cnr) act like torsional dampers. Cmq is the pitch
						damping derivative, Clp is the roll damping derivative and Cnr is the yaw damping
						derivative
						
						The primary control derivatives correspond to deflections of the control surfaces and
						are Cmdelta_e, Cldelta_a and Cndelta_r. Larger values of the control derivatives produce
						larger moments for a given deflection of a control surface.
						
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Propulsion Forces and Moments
						
						Thrust force can be modeled using Bernoulli's principle to calculate the pressure 
						gradient across the propeller area. This model does not take into account propeller
						efficiencies. This model is represented as
						.                                     ((kmotor*delta_t)^2 - Va^2)
						.    fp = 1/2 * rho * Sprop * Cprop * (            0            )
						.                                     (            0            )
						
						
						The torque that the air exerts on the propeller is dependent upon the direction of the
						propeller and the angular speed of the propeller. This torque is given as
						.         (-kTp*(kOmega*delta_t)^2)
						.    mp = (           0           )
						.         (           0           )
						where kTp is a constant determined by experiment and kOmega * delta_t is the propeller 
						speed.
												
												
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Atmospheric Disturbances
						
						Wind speed can be split into two components: a steady ambient component and gust and 
						other atmospheric disturbances component. The steady component is typically given in
						the interital frame and the gust component is typically given in the body frame. The
						total wind speed can therefore be written as
						.            (uw)                          (wns)   (uwg)
						.    V(wb) = (vw) = R(vb)(phi,theta,psi) * (wes) + (vwg)
						.            (ww)                          (wds)   (wwg)
						
						The non-steady gust portion of the wind speed can be modeled by passing white noise
						through a linear time invariant filter given by the von Karmen spectrum. This model
						can be approximated by using Dryden transfer functions. These functions are shown in 
						the book.
						
						Relating wind speed back to airspeed using the wind triangle gives
						.            (ur)   (u - uw)
						.    V(ab) = (vr) = (v - vw)
						.            (wr)   (w - ww)
						
						Also
						.    Va = sqrt(ur^2 + vr^2 + wr^2)
						.    alpha = atan(wr/ur)
						.    beta = asin(vr/Va)
						
						It is through these equations relating wind speed to airspeed that the wind speed 
						enters the aerodynamic equations and affects the motion of the MAV.
					Ch 5: Linear Design Models
						Alternative models can be developed using quaternions to represent MAV attitude. These
						models are more computationally efficient and are free from the gimbal-lock singularity.
						They are more difficult to interpret physically however and so the book uses the Euler
						angles models instead.
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Coordinated Turn - A turn of the aircraft such that the lateral acceleration in the
						body frame is equal to zero.
						
						Summing the forces in the horizontal and vertical planes can show that
						.    chi_dot = g/Vg * tan(phi) * cos(chi - psi)
						where chi is the course angle.
						
						With turning radius R = Vg*cos(gamma)/chi_dot the previous equation can be rearranged as
						.    R = (Vg^2 * cos(gamma)) / (g * tan(phi) * cos(chi - psi))
						where gamma is the flight-path angle (FPA)
						
						In the absence of wind or sideslip (Va=Vg and chi=psi) the equation reduces to
						.    chi_dot = g / Vg * tan(phi)
						
						
						~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						Trim Conditions
						
	Terms
		MAV = Micro-Air Vehicle
		Trim = Aircraft in equilibrium
	Status Updates
		1/23/2015
			I have read the book "Small Unmanned Aircraft: Theory and Practice" excluding the final chapter
			which covers vision-guided navigation. I am currently going back through the book and taking
			notes and getting a grasp on the equations and derivations of the dynamic models and their 
			controls. I plan on finishing the note taking by early next week and will start finding and 
			reviewing the literature on stabilization of the unmanned system.